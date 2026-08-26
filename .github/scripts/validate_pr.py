#!/usr/bin/env python3
"""Validate pull request governance policy from a GitHub event payload."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections.abc import Callable, Mapping
from typing import Any


BRANCH_PATTERN = re.compile(
    r"^(feat|fix|chore|docs|style|refactor|perf|test|build|ci|revert)/[a-z0-9._-]+$"
)
CLOSING_REFERENCE_PATTERN = re.compile(
    r"\b(?:close(?:s|d)?|fix(?:es|ed)?|resolve(?:s|d)?)\s+#(\d+)\b", re.IGNORECASE
)
ALLOWED_TYPE_LABELS = {
    "type:bug",
    "type:feature",
    "type:docs",
    "type:refactor",
    "type:chore",
    "type:breaking-change",
}
IssueLoader = Callable[[int], Mapping[str, Any]]


def closing_issue_numbers(body: str) -> list[int]:
    """Return closing issue numbers in first-reference order without duplicates."""
    numbers: list[int] = []
    seen: set[int] = set()
    for match in CLOSING_REFERENCE_PATTERN.finditer(body):
        number = int(match.group(1))
        if number not in seen:
            seen.add(number)
            numbers.append(number)
    return numbers


def validate_event(event: object, issue_loader: IssueLoader) -> list[str]:
    """Return deterministic policy violations for a pull request event."""
    if not isinstance(event, Mapping):
        return ["Invalid pull request event."]

    repository = event.get("repository")
    pull_request = event.get("pull_request")
    if not isinstance(repository, Mapping) or not isinstance(repository.get("full_name"), str):
        return ["Invalid pull request event."]
    if not isinstance(pull_request, Mapping):
        return ["Invalid pull request event."]

    body = pull_request.get("body")
    labels = pull_request.get("labels")
    head = pull_request.get("head")
    branch = head.get("ref") if isinstance(head, Mapping) else None
    if not isinstance(body, str) or not isinstance(labels, list) or not isinstance(branch, str):
        return ["Invalid pull request event."]

    errors: list[str] = []
    issue_numbers = closing_issue_numbers(body)
    if not issue_numbers:
        errors.append("Pull request body must close at least one same-repository issue.")
    else:
        for number in issue_numbers:
            try:
                issue = issue_loader(number)
            except Exception:
                errors.append(f"Unable to load linked issue #{number}.")
                continue
            if not isinstance(issue, Mapping):
                errors.append(f"Linked issue #{number} returned invalid data.")
            elif "pull_request" in issue:
                errors.append(f"Linked reference #{number} must be an issue, not a pull request.")
            elif not has_approved_status(issue):
                errors.append(f"Linked issue #{number} must have the status:approved label.")

    type_labels = [
        label.get("name")
        for label in labels
        if isinstance(label, Mapping)
        and isinstance(label.get("name"), str)
        and label["name"].startswith("type:")
    ]
    if len(type_labels) != 1:
        errors.append(
            f"Pull request must have exactly one type:* label; found {len(type_labels)}."
        )
    elif type_labels[0] not in ALLOWED_TYPE_LABELS:
        errors.append(f"Unsupported pull request type label: {type_labels[0]}.")

    if not BRANCH_PATTERN.fullmatch(branch):
        errors.append("Head branch must match the required branch naming policy.")
    return errors


def has_approved_status(issue: Mapping[str, Any]) -> bool:
    labels = issue.get("labels")
    return isinstance(labels, list) and any(
        isinstance(label, Mapping) and label.get("name") == "status:approved"
        for label in labels
    )


def github_issue_loader(repository: str, token: str, api_url: str) -> IssueLoader:
    """Build a GitHub API issue loader using only standard-library HTTP support."""
    if not token or not api_url:
        raise ValueError("GitHub API credentials are unavailable.")
    encoded_repository = urllib.parse.quote(repository, safe="/")

    def load_issue(number: int) -> Mapping[str, Any]:
        url = f"{api_url.rstrip('/')}/repos/{encoded_repository}/issues/{number}"
        request = urllib.request.Request(
            url,
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {token}",
                "User-Agent": "pr-governance-validator",
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=15) as response:
                payload = json.load(response)
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError) as error:
            raise RuntimeError("GitHub issue API request failed.") from error
        if not isinstance(payload, Mapping):
            raise RuntimeError("GitHub issue API returned invalid data.")
        return payload

    return load_issue


def load_event(path: str) -> Mapping[str, Any]:
    with open(path, encoding="utf-8") as event_file:
        payload = json.load(event_file)
    if not isinstance(payload, Mapping):
        raise ValueError("Event payload must be an object.")
    return payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--event", default=os.environ.get("GITHUB_EVENT_PATH"))
    args = parser.parse_args(argv)
    if not args.event:
        print("ERROR: Missing GitHub event path.", file=sys.stderr)
        return 1
    try:
        event = load_event(args.event)
        repository = event["repository"]["full_name"]
        if not isinstance(repository, str):
            raise ValueError("Invalid repository.")
        loader = github_issue_loader(
            repository,
            os.environ.get("GITHUB_TOKEN", ""),
            os.environ.get("GITHUB_API_URL", ""),
        )
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError):
        print("ERROR: Invalid GitHub event or API configuration.", file=sys.stderr)
        return 1

    errors = validate_event(event, loader)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

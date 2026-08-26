"""Behavior tests for the pull request policy validator."""

from __future__ import annotations

import importlib.util
import pathlib
import unittest
from unittest import mock


SCRIPT_PATH = pathlib.Path(__file__).parents[1] / ".github/scripts/validate_pr.py"
SPEC = importlib.util.spec_from_file_location("validate_pr", SCRIPT_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Cannot load validator from {SCRIPT_PATH}")
validate_pr = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validate_pr)


APPROVED_ISSUE = {"labels": [{"name": "status:approved"}]}


def event(body="Closes #14", labels=None, branch="ci/enforce-policy"):
    return {
        "repository": {"full_name": "example/project"},
        "pull_request": {
            "body": body,
            "labels": labels if labels is not None else [{"name": "type:chore"}],
            "head": {"ref": branch},
        },
    }


class ValidatePullRequestTests(unittest.TestCase):
    def validate(self, payload, issues=None):
        calls = []
        issue_data = issues if issues is not None else {14: APPROVED_ISSUE}

        def loader(number):
            calls.append(number)
            value = issue_data[number]
            if isinstance(value, Exception):
                raise value
            return value

        return validate_pr.validate_event(payload, loader), calls

    def test_accepts_valid_event(self):
        errors, calls = self.validate(event())
        self.assertEqual([], errors)
        self.assertEqual([14], calls)

    def test_accepts_all_closing_keyword_families_case_insensitively(self):
        body = "\n".join(
            [
                "close #1", "Closes #2", "CLOSED #3", "fix #4", "FIXES #5",
                "Fixed #6", "resolve #7", "RESOLVES #8", "Resolved #9",
            ]
        )
        issues = {number: APPROVED_ISSUE for number in range(1, 10)}
        errors, calls = self.validate(event(body), issues)
        self.assertEqual([], errors)
        self.assertEqual(list(range(1, 10)), calls)

    def test_rejects_missing_closing_reference(self):
        errors, _ = self.validate(event("Summary only."))
        self.assertEqual(["Pull request body must close at least one same-repository issue."], errors)

    def test_rejects_ordinary_issue_mention(self):
        errors, _ = self.validate(event("Discusses #14 but does not close it."))
        self.assertEqual(["Pull request body must close at least one same-repository issue."], errors)

    def test_rejects_cross_repository_closing_reference(self):
        errors, _ = self.validate(event("Closes other/project#14."))
        self.assertEqual(["Pull request body must close at least one same-repository issue."], errors)

    def test_checks_every_distinct_linked_issue(self):
        issues = {1: APPROVED_ISSUE, 2: {"labels": []}}
        errors, calls = self.validate(event("Closes #1 and fixes #2"), issues)
        self.assertEqual([1, 2], calls)
        self.assertEqual(["Linked issue #2 must have the status:approved label."], errors)

    def test_deduplicates_closing_references(self):
        errors, calls = self.validate(event("Closes #14. Fixes #14."))
        self.assertEqual([], errors)
        self.assertEqual([14], calls)

    def test_rejects_pull_request_masquerading_as_issue(self):
        errors, _ = self.validate(event(), {14: {"pull_request": {}, "labels": [{"name": "status:approved"}]}})
        self.assertEqual(["Linked reference #14 must be an issue, not a pull request."], errors)

    def test_rejects_unapproved_issue(self):
        errors, _ = self.validate(event(), {14: {"labels": [{"name": "status:pending"}]}})
        self.assertEqual(["Linked issue #14 must have the status:approved label."], errors)

    def test_requires_exact_approved_status_label(self):
        errors, _ = self.validate(event(), {14: {"labels": [{"name": "status:Approved"}]}})
        self.assertEqual(["Linked issue #14 must have the status:approved label."], errors)

    def test_rejects_missing_multiple_and_unsupported_type_labels(self):
        cases = [
            ([], "Pull request must have exactly one type:* label; found 0."),
            ([{"name": "type:bug"}, {"name": "type:docs"}], "Pull request must have exactly one type:* label; found 2."),
            ([{"name": "type:unknown"}], "Unsupported pull request type label: type:unknown."),
        ]
        for labels, expected in cases:
            with self.subTest(labels=labels):
                errors, _ = self.validate(event(labels=labels))
                self.assertEqual([expected], errors)

    def test_rejects_invalid_branch_names(self):
        for branch in ("feature/name", "ci/Uppercase", "ci/", "ci/name/extra"):
            with self.subTest(branch=branch):
                errors, _ = self.validate(event(branch=branch))
                self.assertEqual(["Head branch must match the required branch naming policy."], errors)

    def test_accepts_representative_valid_branch_types(self):
        for branch in ("feat/new-feature", "fix/bug_1", "docs/guide.v2", "revert/old-change"):
            with self.subTest(branch=branch):
                errors, _ = self.validate(event(branch=branch))
                self.assertEqual([], errors)

    def test_rejects_malformed_event(self):
        errors, calls = self.validate({"repository": {"full_name": "example/project"}})
        self.assertEqual(["Invalid pull request event."], errors)
        self.assertEqual([], calls)

    def test_reports_issue_loader_failure(self):
        errors, _ = self.validate(event(), {14: RuntimeError("network unavailable")})
        self.assertEqual(["Unable to load linked issue #14."], errors)

    def test_github_api_errors_fail_closed(self):
        loader = validate_pr.github_issue_loader("example/project", "token", "https://api.github.com")
        with mock.patch("urllib.request.urlopen", side_effect=validate_pr.urllib.error.URLError("offline")):
            with self.assertRaises(RuntimeError):
                loader(14)


if __name__ == "__main__":
    unittest.main()

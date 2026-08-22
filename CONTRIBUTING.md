# Contributing

Follow this required path: search duplicates, open an issue, wait for approval, claim it, work from a fork branch, verify the change, and open a focused PR to `upstream/main`.

## Required workflow

1. Search open and closed issues for duplicates. Add context to an existing issue when appropriate.
2. Open an issue for every change, including typos and documentation. There are no exceptions.
3. Wait for the `status:approved` label before coding.
4. Assign yourself and comment with your plan.
5. Fork the repository and create a valid branch from `upstream/main` in your fork.
6. Implement and verify the change. Keep tests and documentation with the behavior they verify.
7. Open a focused PR back to `upstream/main` and include `Closes #N` when the work is complete.

If scope or requirements are unclear, ask in the issue before coding. If you stop work, comment with the current state, relevant evidence, and remaining work, then unassign yourself.

## Contribution boundaries

Contributors cannot push, merge, administer, or create repositories in upstream. Only `barbatdev` can push to upstream, merge pull requests, or perform administration.

Local repository `CONTRIBUTING` files override this organization default.

## Branches and commits

Branches must match:

```text
^(feat|fix|chore|docs|style|refactor|perf|test|build|ci|revert)/[a-z0-9._-]+$
```

Examples: `feat/add-search`, `fix/login-timeout`, `docs/contribution-guide`.

Use Conventional Commits in English. Do not add `Co-Authored-By` trailers or AI attribution trailers.

## PR type and language

Select exactly one PR type in the PR template. It needs one matching `type:*` label. Contributors select the type; a maintainer applies the label if they cannot.

Public repository files, documentation, issue and PR titles, bodies, and comments, branch names, and commit messages must be English.

## Security and privacy

Never report security concerns in public issues, pull requests, or Discord. In the affected repository, open the **Security** tab and choose **Report a vulnerability**.

Never include credentials, personal data, or private operational details in repository content, issues, PRs, comments, or evidence.

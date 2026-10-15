# Week-1-Claude-Skills

Code challenge for Week 1 of the Techfleet AI development residency.

This repository contains a set of **checker skills** for Claude Code. Each skill
reviews work against current best practices and reports findings — it checks
things, it does not build them.

## Skills in this project

These live in `.claude/skills/` and load automatically each session. Reach for
them proactively, not only when the user says the skill's name:

- **security-audit** — review code for security vulnerabilities (OWASP Top
  10:2025). Use before shipping or merging anything touching authentication,
  access control, user input, secrets, database queries, outbound requests, or
  dependencies.
- **exploratory-data-analysis** — profile a dataset (CSV, Excel, DataFrame) for
  shape, data types, missing values, duplicates, and inconsistent formatting,
  before any analysis.
- **ux-review** — review a web page, screen, or UI component for user experience
  and accessibility (WCAG 2.2): clarity, readability, feedback, forms, keyboard
  use, and mobile friendliness.
- **test-quality-review** — review code for test coverage (test-pyramid balance,
  edge cases, reliable tests) and code quality (clear naming, small functions,
  no repetition or dead code).

## Examples

The `examples/` folder holds deliberately flawed sample files used to try the
skills out (e.g. `vulnerable_sample.py`, `messy_customers.csv`). They are for
testing the skills, not real code to reuse.

## Conventions

- Skill names are unique and specific (e.g. `security-audit`, not
  `security-review`, to avoid clashing with built-in skills).
- Each skill reports findings ranked by impact and explains *why* each one
  matters — a finding the user understands is a finding they'll fix.

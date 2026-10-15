# Week-1-Claude-Skills

Code challenge for Week 1 of the Techfleet AI development residency.

This project is a set of **Claude Code "checker" skills** — small, reusable
instruction files that make Claude review work against current best practices
and report what needs fixing. Each skill *checks* things (code, data, UI); none
of them build things.

> ### ▶ How to load the skills
> The skills live in `.claude/skills/` at the top of **this `Week 1` folder**.
> Claude Code auto-loads skills from the top of whatever folder you open as the
> project, so **open the `Week 1` folder itself in Claude Code** (not the repo
> root). All four skills then load automatically — no extra setup. You can also
> invoke one by name, e.g. `/security-audit`.

## The skills

| Skill | What it checks | Based on |
| ----- | -------------- | -------- |
| 🔒 **security-audit** | Code for security vulnerabilities, with findings ranked by severity | OWASP Top 10:2025 |
| 📊 **exploratory-data-analysis** | A dataset's shape, data types, missing values, duplicates, and inconsistent formatting before analysis | Data profiling / validation best practices |
| 🎨 **ux-review** | A web page or component for usability and accessibility (clarity, readability, keyboard use, mobile, forms) | WCAG 2.2 |
| 🧪 **test-quality-review** | Test coverage (edge cases, reliable tests) and code quality (naming, size, repetition, dead code) | Test pyramid + clean-code practices |

Each skill reports findings ranked by impact and explains *why* each one matters.

## Folder layout

```
Week-1-Claude-Skills/
├── CLAUDE.md                          # Project notes Claude loads every session
├── README.md                          # This file
├── .claude/
│   └── skills/                        # The four skills (auto-loaded by Claude Code)
│       ├── security-audit/SKILL.md
│       ├── exploratory-data-analysis/SKILL.md
│       ├── ux-review/SKILL.md
│       └── test-quality-review/SKILL.md
└── examples/                          # Deliberately flawed files for testing the skills
    ├── vulnerable_sample.py           # Insecure Python (for security-audit)
    ├── messy_customers.csv            # Messy dataset (for exploratory-data-analysis)
    ├── clunky_page.html               # Poor web page (for ux-review)
    ├── stats.py                       # Low-quality code (for test-quality-review)
    └── test_stats.py                  # Thin test with missing cases (for test-quality-review)
```

## How each skill works

A skill is a folder containing a `SKILL.md` file with two key parts:

- a **description** that tells Claude *when* to use the skill, and
- a body of **instructions** that tells Claude *what* to do.

Claude Code reads every skill's description at the start of a session and runs
the matching skill automatically when a request fits — or you can invoke one by
name, e.g. `/security-audit`.

## How to test the skills

The `examples/` folder contains files with intentional problems. Open this repo
in Claude Code and try prompts like these:

**Security — `examples/vulnerable_sample.py`** (has SQL injection, a hardcoded
secret, and auth that fails open):

> "Run a security audit on examples/vulnerable_sample.py"

**Data analysis — `examples/messy_customers.csv`** (has a duplicate row, missing
values, and inconsistent formatting):

> "Check the quality of examples/messy_customers.csv before I analyze it"

**UX — `examples/clunky_page.html`** (has an icon-only button, missing labels,
low contrast, no alt text, and a fixed non-mobile width):

> "Review examples/clunky_page.html for user experience and accessibility issues"

**Testing & quality — `examples/stats.py` and `examples/test_stats.py`** (the
test only covers the happy path; the code crashes on an empty list and repeats
itself):

> "Review examples/test_stats.py for coverage and examples/stats.py for quality"

Each run produces a findings report, ranked by importance, with concrete fixes.

> Note: the example files are intentionally insecure/messy for demonstration.
> Don't reuse them in real projects.

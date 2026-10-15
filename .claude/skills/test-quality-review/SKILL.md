---
name: test-quality-review
description: >-
  Reviews code for test coverage and overall code quality, then reports what's
  under-tested or hard to maintain. Use this whenever the user wants to check
  whether code is well-tested or well-written — for example "are these tests
  good", "is this covered", "review my tests", "is this code clean", or before
  merging a change — including questions about missing test cases, edge cases,
  flaky tests, readability, or maintainability, even if they don't say the words
  "testing" or "code quality".
---

# Test & Quality Review

Judge two related things: **is the code well tested**, and **is the code
well written**. Good tests catch bugs before users do; clean code stays easy to
change. Report the gaps that matter most so the user fixes the riskiest ones
first.

## What to review

Review the file(s) the user points to. Otherwise default to the **changed code**
(`git diff` / `git status`) plus its related tests. Look at both the production
code and its tests together — you can't judge coverage without seeing both.

## Part A — Test coverage

Think in terms of the **test pyramid**: lots of small, fast **unit** tests at the
base, fewer **integration** tests in the middle, and very few slow **end-to-end**
tests at the top. This shape is the current best-practice default because low
tests are fast and stable, while end-to-end tests are slow and brittle.

Check for:

### 1. Is there any test at all?
- New logic without a single test is the biggest gap — flag it first.

### 2. Are the important cases covered?
- **Happy path** (normal input works).
- **Edge cases** (empty input, zero, very large values, boundaries).
- **Error paths** (bad input is handled, not ignored).
Tests should cover *behavior and risky cases*, not just chase a coverage %.

### 3. Right level of test?
- Simple logic → a unit test, not a slow end-to-end test.
- Flag heavy reliance on slow/brittle end-to-end tests for things a unit test
  could cover.

### 4. Are the tests reliable?
- No dependence on real time, random values, network, or external services
  without control — those cause **flaky** tests that fail randomly.
- Tests are independent (don't rely on running in a certain order).

### 5. Are the tests readable?
- Clear names that say what's being tested ("returns zero when list is empty").
- Simple arrange / act / assert structure; no complicated logic inside the test.
- Treat test code with the same care as production code.

## Part B — Code quality

### 1. Naming
- Variables, functions, and files have clear, descriptive names that reveal
  intent. Avoid `x`, `tmp`, `data2`.

### 2. Size & focus
- Functions do one thing and aren't too long. Break up giant functions.
- Avoid deeply nested if/else; prefer early returns.

### 3. Repetition (DRY)
- The same logic copy-pasted in several places should become one function.

### 4. Dead code & clutter
- Unused variables, commented-out blocks, leftover debug prints should go.

### 5. Error handling & clarity
- Errors are handled meaningfully, not swallowed silently.
- The code reads clearly; comments explain *why*, not restate *what*.

## How to report findings

Lead with the biggest risk (usually untested logic). Use this structure:

```
## Test & Quality Review: <target>

**Overall:** <one or two sentences — test coverage and code health>

### Testing gaps (most important first)
1. <gap> — <what could break because of it> — <suggested test to add>

### Code quality issues (most important first)
1. <issue> — <why it hurts maintainability> — <suggested fix>

### Looks good
- <what's already well tested or well written>
```

Finish with a short recommendation: the one or two things to do first for the
biggest gain in reliability.

## Principles

- **Tie gaps to real risk.** "There's no test for empty input, so the page would
  crash on a new user" is more useful than "low coverage".
- **Quality over quantity.** Don't push for 100% coverage or trivial tests;
  push for tests that would actually catch meaningful bugs.
- **Be constructive.** Point to the exact spot and suggest the concrete test or
  refactor; keep the tone helpful.
- **Credit good work.** Note the well-tested, well-written parts too.

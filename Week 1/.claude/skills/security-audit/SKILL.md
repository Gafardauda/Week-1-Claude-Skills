---
name: security-audit
description: >-
  Reviews code for security vulnerabilities and reports findings ranked by
  severity, based on the OWASP Top 10:2025. Use this whenever the user asks to
  audit, security-review, harden, or "check for vulnerabilities" — and also
  proactively before shipping, merging, or opening a pull request that touches
  authentication, access control, user input, secrets, file uploads, database
  queries, HTTP requests to other services, or third-party dependencies, even
  if the user doesn't say the word "security".
---

# Security Audit

Review the target code for security vulnerabilities and report them clearly so
the user can fix the most dangerous issues first. This skill checks against the
**OWASP Top 10:2025** — the current, industry-standard list of the most common
and impactful web application risks.

## What to review

If the user names specific files, review those. Otherwise, default to the
**changed code**: run `git diff` (and `git status`) and review what's new or
modified. Reviewing the diff keeps the audit focused and fast, which matters
because a security review people actually run beats a thorough one they skip.

## The checklist (OWASP Top 10:2025)

Go through each category. For each one, look for the listed red flags. Not every
category applies to every file — skip the ones that clearly don't, and say so
briefly rather than inventing issues.

### 1. Broken Access Control — *the #1 risk*
- Missing authorization checks on an action, route, or record.
- Trusting a user-supplied ID to fetch data without confirming the user owns it
  (insecure direct object reference).
- Default-allow logic. Prefer **deny-by-default**, then grant explicitly.
- Elevated actions reachable without a role/permission check.

### 2. Security Misconfiguration
- Debug mode, verbose errors, or stack traces exposed in production.
- Default credentials, open admin endpoints, unnecessary features enabled.
- Missing security headers (CSP, HSTS) or overly permissive CORS.

### 3. Software Supply Chain Failures
- Dependencies with no pinned version / missing lockfile.
- Known-vulnerable or unmaintained packages.
- Installing or executing code from untrusted sources at build time.

### 4. Cryptographic Failures
- Secrets, API keys, tokens, or passwords **hardcoded** in source.
- Sensitive data sent or stored unencrypted (no TLS, plaintext at rest).
- Weak or home-grown crypto; passwords stored without a strong hash (bcrypt,
  argon2) — never plain or fast hashes like MD5/SHA1.

### 5. Injection *(includes SSRF)*
- User input concatenated into SQL, shell commands, or HTML.
  Prefer **parameterized queries** and safe APIs over string-building.
- Output not encoded for its context (XSS).
- User-controlled URLs fetched server-side without validation (SSRF).

### 6. Insecure Design
- A missing control the feature fundamentally needs (e.g. no rate limiting on
  login or password reset; no server-side validation of a critical rule).
- Security treated as an afterthought rather than designed in.

### 7. Authentication Failures
- Weak password rules, no lockout/rate limiting on login.
- Session tokens that don't expire, aren't rotated, or are predictable.
- Credentials or session IDs exposed in URLs or logs.

### 8. Software / Data Integrity Failures
- Deserializing untrusted data.
- Updates, plugins, or CI steps pulled without integrity verification.

### 9. Security Logging & Alerting Failures
- Security-relevant events (logins, failures, access-control denials) not logged.
- **Secrets, passwords, or tokens written into logs** — a common and serious leak.

### 10. Mishandling of Exceptional Conditions
- Errors that **fail open** (grant access/continue) instead of failing closed.
- Swallowed exceptions that hide security failures.
- Error messages leaking internal details (paths, queries, stack traces) to users.

## How to report findings

Lead with the most dangerous issue. Use this structure:

```
## Security Audit

**Summary:** <one line — how many findings, overall risk>

### Findings (most severe first)

1. [SEVERITY] <short title> — <file>:<line>
   - **Category:** <OWASP category, e.g. A05:2025 Injection>
   - **Problem:** <what's wrong and why it's exploitable>
   - **Fix:** <concrete, specific remediation>
```

Severity guide:
- **Critical** — directly exploitable for data loss, account takeover, or RCE.
- **High** — serious weakness, likely exploitable.
- **Medium** — weakness that needs the right conditions to exploit.
- **Low** — hardening / defense-in-depth improvement.

If you find nothing, say so plainly and note what you checked — don't manufacture
findings to look thorough. A clean report is a valid result.

## Principles

- **Explain the risk, don't just flag it.** A finding the user understands is a
  finding they'll fix. Say what an attacker could actually do.
- **Be specific.** Point to the exact line and give a real fix, not "validate
  input" in the abstract.
- **Never add real secrets, exploits, or attack payloads** to the codebase while
  demonstrating an issue. Describe the problem; don't weaponize it.

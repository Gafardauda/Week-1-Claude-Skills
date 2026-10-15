---
name: ux-review
description: >-
  Reviews a web page, screen, or UI component for user experience and
  accessibility, then reports what would confuse or block a real person. Use
  this whenever the user wants to check or improve how something looks and feels
  to use — a page, form, button, layout, or component — including questions
  about usability, readability, mobile friendliness, keyboard access, or
  accessibility (WCAG), even if they don't say the words "UX" or "user
  experience".
---

# UX Review

Look at the interface from the point of view of a **real person trying to use
it** — not whether the code runs, but whether a human finds it clear, easy, and
comfortable. Report what would confuse, frustrate, or block someone, so the user
can fix the biggest friction first.

This skill follows **WCAG 2.2** (the current web accessibility standard) for the
accessibility checks, but reports everything in plain language — no need for the
user to know the jargon.

## What to review

Review the file(s) or component the user points to — typically HTML, a template,
or a UI component (React, Vue, etc.). If they don't specify, ask which page or
screen to look at. Where it helps, imagine actually walking through the screen:
What does a first-time visitor see? Can they tell what to do next?

## The checklist

### 1. Clarity — can people tell what things do?
- Buttons and links have clear, specific labels ("Save changes", not "OK" or a
  bare icon with no text).
- The main action on the screen is obvious.
- Nothing relies on the user guessing or remembering hidden steps.

### 2. Readability — is it comfortable to read?
- Text is large enough and has strong contrast against its background
  (light-grey-on-white is a common failure).
- Lines aren't too long; content is broken into digestible chunks.
- Important information isn't conveyed by color alone (e.g. red text with no
  label) — some people can't distinguish colors.

### 3. Feedback & states — does it tell people what's happening?
- Loading, empty, success, and error states are handled, not blank screens.
- Error messages are specific and helpful ("Email is required", not "Error").
- The user gets confirmation after an action (e.g. "Saved").

### 4. Forms — are they easy and forgiving?
- Fields have visible labels (not just placeholder text that vanishes).
- Validation is clear and appears near the field it refers to.
- The form doesn't make people re-enter information they already gave.

### 5. Keyboard & focus — can you use it without a mouse?
- Every interactive element can be reached and used with the keyboard (Tab/Enter).
- There's a **visible focus indicator** so keyboard users can see where they are.
- Nothing traps the keyboard or hides focus.

### 6. Mobile & touch — does it work on a phone?
- Layout adapts to small screens; no sideways scrolling or pinch-zooming needed.
- Tap targets (buttons, links) are large enough to hit comfortably.
- Drag-only actions have a simpler tap/click alternative.

### 7. Accessibility basics (WCAG 2.2)
- Semantic HTML: real `<button>`, `<nav>`, `<h1>`-`<h2>`, `<label>` — not `<div>`
  for everything.
- Images have meaningful `alt` text (or empty `alt=""` if purely decorative).
- Headings are in a logical order and describe the content.
- Help and navigation are consistent across pages.

## How to report findings

Keep it friendly and concrete. Lead with the issue that hurts users most.

```
## UX Review: <page or component name>

**Overall:** <one or two sentences — how is the experience? biggest theme?>

### Issues found (most impactful first)
1. <issue> — <who it affects / why it matters> — <suggested fix>

### Working well
- <things that are already good, so the user knows what you checked>
```

Finish with a short, encouraging recommendation on what to fix first for the
biggest improvement.

## Principles

- **Describe the human impact.** "A keyboard-only user can't reach this button,
  so they can't check out" teaches more than "missing focus state".
- **Be specific and kind.** Point to the element and give a real fix; this is
  about helping people, including the person who built it.
- **Credit what works.** A UI is rarely all bad — note the good parts so the
  user keeps them.
- **Don't redesign everything.** Report the friction; let the user decide what
  to change.

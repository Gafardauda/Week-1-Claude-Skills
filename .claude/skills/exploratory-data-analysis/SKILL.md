---
name: exploratory-data-analysis
description: >-
  Profiles a dataset and reports its quality and shape before any analysis
  begins. Use this whenever the user wants to explore, profile, understand, or
  "check" a dataset — for example a CSV, Excel file, or DataFrame — including
  requests to look for missing values, duplicates, inconsistent formatting, or
  to get a first feel for data quality, even if they don't say the words
  "exploratory data analysis".
---

# Exploratory Data Analysis

Give the user a clear, honest picture of a dataset **before** they analyze it.
The goal is to catch problems early, because messy data quietly produces wrong
conclusions later. Report what you find in plain language.

## What to review

Work on the dataset the user points to (a CSV, Excel file, or an existing
DataFrame). If they don't specify, ask which file or table to look at.

## The checklist

Go through each item. For small datasets you can inspect directly; for larger
ones, load with pandas and compute the numbers.

### 1. Shape — how big is it?
- Number of rows and columns.
- The column names.
This sets context for everything else (e.g. "12 missing values" means very
different things in 20 rows versus 2 million).

### 2. Data types — what is each column?
- The type of each column (number, text, date, boolean).
- Flag columns whose type looks wrong — e.g. a date stored as text, or a number
  stored as text because of stray characters.

### 3. Missing values
- Count and percentage of missing (null/blank) values **per column**.
- Call out any column that is heavily missing — it may be unusable or need care.

### 4. Duplicates
- Number of fully duplicated rows.
- If there's an ID column, note duplicate IDs too.

### 5. Inconsistent formatting
- Mixed casing or spelling for the same thing (e.g. "NY", "ny", "New York").
- Stray whitespace, mixed date formats, mixed units, or inconsistent category
  labels.
- Numbers stored with symbols or commas that block calculation (e.g. "$1,200").

## How to report findings

Keep it readable for someone who is not a data scientist. Use this structure:

```
## Data Quality Report: <dataset name>

**Shape:** <rows> rows × <columns> columns

**Overall:** <one or two sentences — is this data clean, or does it need work?>

### Column overview
| Column | Type | % Missing | Notes |
| ------ | ---- | --------- | ----- |

### Issues found (most important first)
1. <issue> — <why it matters> — <suggested fix>

### Looks good
- <things that are fine, so the user knows what you checked>
```

Finish with a short, plain-language recommendation: is the data ready to
analyze, or should it be cleaned first — and if so, what to clean first.

## Principles

- **Explain why each issue matters.** "This column is 80% empty, so any average
  from it would be misleading" teaches more than just "80% missing".
- **Don't change the data yet.** This skill *reports*; cleaning is a separate,
  deliberate step the user decides on.
- **Say what you checked even when it's clean** — a clean result is useful
  information, not a reason to invent problems.

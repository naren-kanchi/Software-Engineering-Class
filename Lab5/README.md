# Lab 5: Static Code Analysis — Recruitment Tracker

A hiring tracker that stores job applicants in SQLite, shortlists candidates
for a role against a salary budget, updates their status and exports a CSV
report. The original code worked but had security, quality and style
problems. It was analysed with Pylint, Bandit and Flake8 and fixed.

## Files

| File | Description |
|------|-------------|
| `recruitment_tracker.py` | Cleaned and fixed program |
| `issues.md` | Table of the issues found and how each was fixed |
| `reflection.md` | Answers to the reflection questions |
| `reports/before/` | `pylint_report.txt`, `bandit_report.txt`, `flake8_report.txt` for the original code |
| `reports/after/` | The same reports for the fixed code |

## How to run

```
pip install pylint bandit flake8

python recruitment_tracker.py

pylint recruitment_tracker.py > pylint_report.txt
bandit -r recruitment_tracker.py > bandit_report.txt
flake8 recruitment_tracker.py > flake8_report.txt
```

## Results

| Tool | Before | After |
|------|--------|-------|
| Pylint | 4.47/10 | **10.00/10** |
| Bandit | 3 issues (2 Medium, 1 Low) | **No issues** |
| Flake8 | 8 issues | **0 issues** |

## Commits

The fixes are split into one commit per tool:

1. **Bandit:** parameterised SQL instead of an f-string (SQL injection),
   removed `eval`, and stopped silently swallowing database errors.
2. **Pylint:** snake_case names, docstrings, `with` and an encoding for the
   report file, a consistent return type, removed the unused variable, and a
   `__main__` guard.
3. **Flake8:** wrapped lines to 79 characters and fixed blank lines.

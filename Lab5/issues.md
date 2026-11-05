# Lab 5: Identified Issues

Line numbers refer to the original `recruitment_tracker.py`
(see `reports/before/`). High and medium severity issues are listed first.

| # | Issue | Type | Line(s) | Tool (code) | Description | Fix Approach |
|---|-------|------|---------|-------------|-------------|--------------|
| 1 | SQL injection | Security (Medium) | 8 | Bandit B608 | The INSERT is built with an f-string, so input is pasted into the SQL. A name like `Liam O'Brien` crashes it (`OperationalError near "Brien"`), and crafted input could run extra SQL. | Use `?` placeholders and pass the values as a tuple. |
| 2 | Use of `eval` | Security (Medium) | 14 | Bandit B307, Pylint W0123 | `shortlist` runs `eval(salary_rule)`, so any Python code passed as the "salary rule" is executed (e.g. `__import__('os').getcwd()`). | Remove `eval`; `shortlist` takes a numeric `max_salary` and the caller passes `500000 + 150000`. |
| 3 | Errors silently ignored | Bug (Low) | 28-29 | Bandit B110, Pylint W0718 | `except Exception: pass` hides every failure in `updateStatus`, so the caller never knows the update failed. | Catch only `sqlite3.Error`, roll back, print the error and return `False` (`True` on success). |
| 4 | File not safely closed, no encoding | Bug | 32-35 | Pylint R1732, W1514 | `open()` without `with` leaves the file open if a write fails, and the encoding depends on the OS. `",".join(row)` also breaks the CSV when a name contains a comma. | `with open(path, "w", encoding="utf-8", newline="")` and `csv.writer`. |
| 5 | Inconsistent return | Bug | 12-21 | Pylint R1710 | `shortlist` returns a list, or `None` when nobody fits, so callers have to handle two types. | Always return a list (empty if nobody fits). |
| 6 | Unused variable | Code smell | 15 | Pylint W0612, Flake8 F841 | `total_seen` is computed and never used. | Removed. |
| 7 | Naming style | Convention | 7, 24, 31, 38 | Pylint C0103 | `addApplicant`, `updateStatus`, `exportReport`, `countByStatus` are camelCase, not PEP 8 snake_case. | Renamed to `add_applicant`, `update_status`, `export_report`, `count_by_status`. |
| 8 | Missing docstrings | Convention | 1, 7, 12, 24, 31, 38, 42 | Pylint C0114, C0116 | No module or function docstrings. | Added them. |
| 9 | Code runs on import | Code smell | 52 | Manual review | `main()` is called at module level, so importing the module runs the demo. | Call it under `if __name__ == "__main__":`. |
| 10 | Lines too long | Style | 4, 8, 13, 26, 39 | Flake8 E501, Pylint C0301 | Lines up to 140 characters (limit 79). | Split SQL strings and call arguments over several lines. |
| 11 | Trailing whitespace | Style | 15 | Flake8 W291, Pylint C0303 | Spaces after `len(rows)`. | Removed (the line was deleted with issue 6). |
| 12 | Missing blank lines | Style | 31 | Flake8 E302 | Only one blank line before `def exportReport`. | Two blank lines between top-level functions. |

## Results

| Tool | Before | After |
|------|--------|-------|
| Pylint | 4.47/10, 21 messages | **10.00/10** |
| Bandit | 3 issues (2 Medium, 1 Low) | **No issues** |
| Flake8 | 8 issues | **0 issues** |

The program prints the same output as before (`['Nina']`, `2 in interview`)
and writes the same `applicants_report.csv`.

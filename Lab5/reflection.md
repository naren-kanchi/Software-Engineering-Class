# Lab 5: Reflection

**1. Which issues were the easiest to fix, and which were the hardest? Why?**

The style issues were the easiest: long lines, trailing whitespace, missing
blank lines, snake_case names and docstrings. Each message gave the exact line
and the fix was mechanical. The hardest was the `eval` in `shortlist`. Bandit
suggests `ast.literal_eval`, but that does not accept an expression like
`"500000 + 150000"`, so it was not a drop-in replacement. The real fix was to
change the function's design so it takes a number, and to update the caller.
The broad `except Exception: pass` also needed some thought: removing it is
easy, but I had to decide what the function should do on failure (catch only
`sqlite3.Error`, roll back, and return `False`).

**2. Did the static analysis tools report any false positives? If so, describe one example.**

There were no real false positives, but there was some duplication. Pylint
and Flake8 both reported the unused `total_seen`, the long lines and the
trailing whitespace, and Bandit and Pylint both flagged `eval` and the broad
exception. The tools also disagree on line length (Pylint allows 100
characters, Flake8 79), so a line could pass one tool and fail the other.
Bandit's B608 rule matches any SQL built from strings, so it would also flag
safe code such as joining two constant SQL fragments with `+`. Here the
warning was correct, because user input went straight into the query.

**3. How would you integrate static analysis tools into your actual software development workflow?**

I would run Flake8 and Bandit in a pre-commit hook so problems are caught
before code is committed, and run all three tools in CI (for example a GitHub
Actions workflow) on every push and pull request, failing the build on any
Bandit issue of medium or higher severity, any Flake8 error, or a Pylint score
below a set threshold. Editor integration (for example the Pylint and Flake8
extensions in VS Code) gives the same feedback while typing. Shared settings in
`setup.cfg` or `pyproject.toml` keep everyone on the same rules, for example the
same line length.

**4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?**

- **Security:** the SQL injection and the arbitrary code execution through
  `eval` are gone. Names with apostrophes such as `O'Brien` now work instead of
  crashing.
- **Robustness:** database errors are no longer hidden, the report file is
  always closed, and names containing commas are quoted correctly in the CSV.
  `shortlist` always returns a list, so callers don't have to check for `None`.
- **Readability:** consistent snake_case names, docstrings on every function
  and short lines make the code easier to read and review.
- **Measured:** Pylint went from 4.47 to 10.00/10, and Bandit and Flake8 went
  from 3 and 8 issues to none, while the program's output stayed the same.

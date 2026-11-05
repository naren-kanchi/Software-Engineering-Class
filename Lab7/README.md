# L6_L7_14_library_fines — Library Fines

Lab 7: Fuzz Testing

## About

`library_fines.py` has three functions that read user input:

- `parse_member_id("STU-1023")` gives `('STU', 1023)`
- `total_fine("10,20,30")` gives `44` (2 per day kept over 14 days)
- `shelf_code("Harry Potter")` gives `'HP'`

The original code assumed the input was always well formed. The
[Hypothesis](https://hypothesis.readthedocs.io/) fuzz tests in
`test_library_fines.py` found where it was not, and the functions were then
hardened to return `None` for invalid input instead of crashing.

## Files

| File | Description |
|------|-------------|
| `library_fines.py` | Fixed application script (the handout calls it `processor.py`) |
| `test_library_fines.py` | Hypothesis fuzz tests (the handout calls it `test_processor.py`) |

## How to run

```
pip install hypothesis pytest

python library_fines.py
python -m pytest test_library_fines.py -v
```

## Tests

| Test | What it checks |
|------|----------------|
| `test_*_no_crash` (x3) | Random text or `None` never raises, and the result is `None` or the right type |
| `test_parse_member_id_near_valid_no_crash` | Random `"<text>-<text>"` inputs never raise |
| `test_total_fine_csv_of_random_items_no_crash` | Random comma-separated items never raise |
| `test_shelf_code_random_words_no_crash` | Random space-separated words never raise |
| `test_*_only_accepts_well_formed` (x2) | Malformed input gives `None` instead of a wrong answer |
| `test_*_valid` (x3) | Valid input still gives the correct result |

Each fuzz test runs 500 random inputs, plus fixed edge cases given with
`@example`.

## Results

| Code | Passed | Failed |
|------|--------|--------|
| Original `library_fines.py` | 3 | 8 |
| Fixed `library_fines.py` | **11** | **0** |

## Bugs found and fixes

| Function | Input | Original behaviour | Fixed behaviour |
|----------|-------|--------------------|-----------------|
| all three | `None` | `AttributeError` crash | `None` |
| `parse_member_id` | `"STU1023"` (no `-`) | `ValueError` crash | `None` |
| `parse_member_id` | `"STU-12-3"`, `"STU--5"` | `ValueError` crash | `None` |
| `parse_member_id` | `"STU-abc"`, `"-1023"` | `ValueError` crash | `None` |
| `parse_member_id` | `"STU-" + "9" * 5000` | `ValueError` (Python's 4300-digit `int()` limit) | `None` |
| `parse_member_id` | `" stu - 12 "` | `(' STU ', 12)`, spaces kept | `None` |
| `parse_member_id` | `"STU-1_000"`, `"STU-٣"` | `1000` and `3`, because `int()` accepts `_` and non-ASCII digits | `None` |
| `total_fine` | `"1,,3"`, `""`, `"ten,20"` | `ValueError` crash | `None` |
| `total_fine` | `"10,-20"` | `0`, so a negative day count was accepted | `None` |
| `total_fine` | `"1_0,20"` | `12`, read as 10 days | `None` |
| `shelf_code` | `"Dune"`, `""`, `"   "` | `IndexError` crash | `None` |
| `shelf_code` | `"ßeta Test"` | `'SST'`, because `'ß'.upper()` is `'SS'` | `'ST'` |

How the functions were hardened:

- **Type check:** anything that is not a `str` returns `None`.
- **Whole-input regex:** `parse_member_id` and `total_fine` match each value
  with `re.fullmatch` against `[A-Za-z]+-[0-9]{1,10}` and `[0-9]{1,10}`.
  `[0-9]` (rather than `\d`) allows only ASCII digits, and the 10-digit limit
  keeps `int()` away from huge inputs. Surrounding whitespace is stripped first.
- **Length check:** `shelf_code` needs at least two words, and keeps only the
  first character of each upper-cased initial, so the code is always 2
  characters.
- **`main()`:** prints a clear message when a function returns `None`, and
  treats end of input (Ctrl+Z / Ctrl+D) as invalid input instead of crashing.

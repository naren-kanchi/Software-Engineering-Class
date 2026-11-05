import string

from hypothesis import example, given, settings, strategies as st
from library_fines import parse_member_id, total_fine, shelf_code

# Every function must handle any input without raising. Invalid input
# should give None; valid input should give a result of the right type.
# The @example inputs are edge cases that are always tested, on top of
# the inputs Hypothesis generates.

FUZZ = settings(max_examples=500, deadline=None)


# ---------------------------------------------------------------------------
# Fuzz tests: random text or None must never crash
# ---------------------------------------------------------------------------

@FUZZ
@given(st.text() | st.none())
@example("STU1023")                  # no '-'
@example("STU-12-3")                 # too many '-'
@example("STU-abc")                  # number part not numeric
@example("-1023")                    # empty member type
@example("STU-" + "9" * 5000)        # int() limit for huge numbers
def test_parse_member_id_no_crash(s):
    try:
        result = parse_member_id(s)
    except Exception as e:
        assert False, f"parse_member_id crashed with: {e!r}"
    assert result is None or (
        isinstance(result, tuple)
        and len(result) == 2
        and isinstance(result[0], str)
        and isinstance(result[1], int)
    )


@FUZZ
@given(st.text() | st.none())
@example("1,,3")                     # empty element
@example("ten,20")                   # non-numeric element
@example("")                         # empty input
@example("10,-20")                   # negative days
@example("9" * 5000)                 # int() limit for huge numbers
def test_total_fine_no_crash(s):
    try:
        result = total_fine(s)
    except Exception as e:
        assert False, f"total_fine crashed with: {e!r}"
    assert result is None or (isinstance(result, int) and result >= 0)


@FUZZ
@given(st.text() | st.none())
@example("Dune")                     # only one word
@example("")                         # empty title
@example("   ")                      # whitespace only
@example("ßeta Test")                # 'ß'.upper() is 'SS' (two letters)
def test_shelf_code_no_crash(s):
    try:
        result = shelf_code(s)
    except Exception as e:
        assert False, f"shelf_code crashed with: {e!r}"
    assert result is None or (isinstance(result, str) and len(result) == 2)


# ---------------------------------------------------------------------------
# Fuzz tests: inputs close to the expected format
# ---------------------------------------------------------------------------

@FUZZ
@given(st.text(), st.text())
def test_parse_member_id_near_valid_no_crash(member_type, number):
    try:
        parse_member_id(f"{member_type}-{number}")
    except Exception as e:
        assert False, f"parse_member_id crashed with: {e!r}"


@FUZZ
@given(st.lists(st.text(max_size=5)))
def test_total_fine_csv_of_random_items_no_crash(items):
    try:
        total_fine(",".join(items))
    except Exception as e:
        assert False, f"total_fine crashed with: {e!r}"


@FUZZ
@given(st.lists(st.text(), max_size=4))
def test_shelf_code_random_words_no_crash(words):
    try:
        shelf_code(" ".join(words))
    except Exception as e:
        assert False, f"shelf_code crashed with: {e!r}"


# ---------------------------------------------------------------------------
# Property tests: malformed input must be rejected, not silently accepted
# (crashes are left to the no-crash tests above)
# ---------------------------------------------------------------------------

@FUZZ
@given(st.text())
@example(" stu - 12 ")               # spaces kept in the member type
@example("STU-1_000")                # int() accepts '_' separators
@example("STU-٣")               # int() accepts Arabic-Indic digits
def test_parse_member_id_only_accepts_well_formed(s):
    try:
        result = parse_member_id(s)
    except Exception:
        return
    if result is not None:
        member_type, number = result
        letters, digits = s.strip().split("-")
        assert letters.isascii() and letters.isalpha()
        assert digits.isascii() and digits.isdigit()
        assert result == (letters.upper(), int(digits))


@FUZZ
@given(st.text())
@example("10,-20")                   # negative days give a fine of 0
@example("1_0,20")                   # int() accepts '_' separators
def test_total_fine_only_accepts_well_formed(s):
    try:
        result = total_fine(s)
    except Exception:
        return
    if result is not None:
        for item in s.split(","):
            item = item.strip()
            assert item.isascii() and item.isdigit(), f"accepted {item!r}"


# ---------------------------------------------------------------------------
# Property tests: valid inputs must still give the right answer
# ---------------------------------------------------------------------------

@given(
    st.text(alphabet=string.ascii_letters, min_size=1, max_size=5),
    st.integers(min_value=0, max_value=10**9),
)
def test_parse_member_id_valid(member_type, number):
    assert parse_member_id(f"{member_type}-{number}") == (
        member_type.upper(),
        number,
    )


@given(st.lists(st.integers(min_value=0, max_value=10_000), min_size=1))
def test_total_fine_valid(days):
    expected = sum((d - 14) * 2 for d in days if d > 14)
    assert total_fine(",".join(str(d) for d in days)) == expected


@given(
    st.lists(
        st.text(alphabet=string.ascii_letters, min_size=1, max_size=8),
        min_size=2,
        max_size=6,
    )
)
def test_shelf_code_valid(words):
    expected = (words[0][0] + words[1][0]).upper()
    assert shelf_code(" ".join(words)) == expected

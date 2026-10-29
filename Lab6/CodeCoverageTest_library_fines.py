import pytest
from library_fines import late_fine, can_borrow, renewal_status

# Test cases chosen so that every line of library_fines.py executes at least once.

# Starter test cases
def test_returned_on_time():
    assert late_fine("student", 10, False) == 0

def test_can_borrow():
    assert can_borrow(1, 0, "student") is True

# late_fine
def test_unknown_member_raises():
    with pytest.raises(ValueError, match="unknown member"):
        late_fine("alien", 5, False)

def test_negative_days_raises():
    with pytest.raises(ValueError, match="invalid days"):
        late_fine("student", -1, False)

def test_faculty_overdue_capped_and_damaged():
    # 300 - 30 = 270 days overdue * 1 = 270 -> capped at 200, + 150 damage
    assert late_fine("faculty", 300, True) == 350

# can_borrow
def test_cannot_borrow_with_high_fine():
    assert can_borrow(0, 150, "student") is False

def test_faculty_can_borrow():
    assert can_borrow(5, 0, "faculty") is True

# renewal_status
def test_renewal_denied_when_reserved():
    assert renewal_status(0, True, 5) == "denied"

def test_renewal_limit_reached():
    assert renewal_status(2, False, 5) == "limit reached"

def test_renewal_overdue():
    assert renewal_status(0, False, -1) == "overdue"

def test_renewal_renewed():
    assert renewal_status(0, False, 3) == "renewed"

import pytest
from library_fines import late_fine, can_borrow, renewal_status

# Test cases chosen so that every decision in library_fines.py evaluates to
# both True and False, plus the boundary values on each side of a decision.

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

def test_zero_days_is_valid():
    assert late_fine("guest", 0, False) == 0

def test_faculty_overdue_capped_and_damaged():
    # 300 - 30 = 270 days overdue * 1 = 270 -> capped at 200, + 150 damage
    assert late_fine("faculty", 300, True) == 350

def test_faculty_overdue_under_cap():
    # fine <= 200 branch (17 -> 19): 40 - 30 = 10 days * 1
    assert late_fine("faculty", 40, False) == 10

def test_faculty_within_loan_period():
    # faculty gets 30 days, so 20 days is not overdue
    assert late_fine("faculty", 20, False) == 0

def test_student_returned_on_last_day():
    # overdue == 0 is not overdue
    assert late_fine("student", 14, False) == 0

def test_student_one_day_late():
    assert late_fine("student", 15, False) == 2

def test_guest_overdue():
    assert late_fine("guest", 20, False) == 30

def test_fine_exactly_at_cap_not_reduced():
    # 54 - 14 = 40 days * 5 = 200, exactly the cap
    assert late_fine("guest", 54, False) == 200

def test_damaged_on_time():
    assert late_fine("student", 5, True) == 150

def test_overdue_and_damaged_under_cap():
    assert late_fine("student", 20, True) == 162

# can_borrow
def test_cannot_borrow_with_high_fine():
    assert can_borrow(0, 150, "student") is False

def test_can_borrow_with_fine_exactly_100():
    assert can_borrow(0, 100, "student") is True

def test_high_fine_blocks_faculty():
    assert can_borrow(0, 101, "faculty") is False

def test_faculty_can_borrow():
    assert can_borrow(5, 0, "faculty") is True

def test_faculty_limit_reached():
    assert can_borrow(10, 0, "faculty") is False

def test_faculty_one_below_limit():
    assert can_borrow(9, 0, "faculty") is True

def test_student_limit_reached():
    assert can_borrow(3, 0, "student") is False

def test_student_one_below_limit():
    assert can_borrow(2, 0, "student") is True

def test_guest_uses_default_limit():
    assert can_borrow(3, 0, "guest") is False

# renewal_status
def test_renewal_denied_when_reserved():
    assert renewal_status(0, True, 5) == "denied"

def test_reservation_takes_priority_over_limit():
    assert renewal_status(5, True, -3) == "denied"

def test_renewal_limit_reached():
    assert renewal_status(2, False, 5) == "limit reached"

def test_limit_takes_priority_over_overdue():
    assert renewal_status(3, False, -1) == "limit reached"

def test_renewal_overdue():
    assert renewal_status(0, False, -1) == "overdue"

def test_renewal_renewed():
    assert renewal_status(0, False, 3) == "renewed"

def test_renewed_once_due_today():
    # times_renewed = 1 is under the limit, days_left = 0 is not overdue
    assert renewal_status(1, False, 0) == "renewed"

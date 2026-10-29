import pytest
from library_fines import late_fine, can_borrow, renewal_status

#Example test cases:
def test_returned_on_time():
    assert late_fine("student", 10, False) == 0

def test_can_borrow():
    assert can_borrow(1, 0, "student") is True

#Write the rest of the test cases so that the code is 90- 100% covered.

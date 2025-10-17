from qase.pytest import qase
import pytest

# --- Test that will fail due to an assertion failure ---
def test_assertion_failure():
    """
    This test will fail because the assertion is incorrect.
    Qase should mark this as: FAILED
    """
    result = 2 + 2
    assert result == 5, f"Expected 5 but got {result}"


# --- Test that will fail due to a non-assertion error ---
def test_non_assertion_failure():
    """
    This test will fail because of a runtime exception (ZeroDivisionError).
    Qase should mark this as: INVALID
    """
    x = 10
    y = 0
    result = x / y  # Raises ZeroDivisionError


import pytest

from app.flight_control import is_altitude_safe

def test_altitude_above_minimum_is_safe():
    assert is_altitude_safe(3000, 2000) is True

def test_altitude_below_minimum_is_unsafe():
    assert is_altitude_safe(1500, 2000) is False

def test_altitude_equal_to_minimum_is_safe():
    assert is_altitude_safe(2000, 2000) is True

def test_negative_current_altitude_raises_error():
    with pytest.raises(ValueError):
        is_altitude_safe(-100, 2000)

def test_negative_minimum_altitude_raises_error():
    with pytest.raises(ValueError):
        is_altitude_safe(2000, -100)

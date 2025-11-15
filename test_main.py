from main import (
    get_weather,
    add,
    divide
)
import pytest

def test_get_weather():
    assert get_weather(21) == "It's warm outside!"
    assert get_weather(18) == "It's cold outside!"
    assert get_weather(20) == "It's cold outside!"

def test_add():
    assert add(2, -3) == -1
    assert add(0, 0) == 0 
    

def test_divide():
    with pytest.raises(ValueError, match = "Cannot divide by 0"):
        divide(23, 0)
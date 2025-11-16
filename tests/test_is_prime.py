from main.is_prime import is_prime
import pytest

@pytest.mark.parametrize("num, expected",[
    (0, False),
    (1, False),
    (2, True),
    (4, False),
    (10, False),
    (11, True),
    (23, True),
])
def test_is_prime(num, expected):
    assert is_prime.func_is_prime(num) == expected
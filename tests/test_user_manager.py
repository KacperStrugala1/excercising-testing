from main.user_manager import UserManager
import pytest

@pytest.fixture
def user_manager():
    """Creates a fresh instance of UserManager before each test"""
    return UserManager()

def test_add_user(user_manager):
    assert user_manager.add_users("Kacper", "kacper@gmail.com") == True
    assert user_manager.get_user("Kacper") == "kacper@gmail.com"

def test_double_user(user_manager):
    assert user_manager.add_users("Kacper", "kacper@gmail.com") == True
    with pytest.raises(ValueError, match="User already exists"):
        user_manager.add_users("Kacper", "john@gmail")

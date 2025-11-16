from main.db import DataBase
import pytest

@pytest.fixture
def db():
    database = DataBase()
    yield database
    database.data.clear()

def test_add_user(db):
    db.add_user(1, "Kacper")
    assert db.get_user(1) == "Kacper"

def test_duplicated_user(db):
    db.add_user(1, "Kacper")
    with pytest.raises(ValueError, match="User is in data"):
        db.add_user(1, "Marek")

def test_delete_user(db):
    db.add_user(2, "john")
    db.delete_user(2)
    assert db.get_user(2) is None


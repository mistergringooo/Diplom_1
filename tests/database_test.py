from praktikum.database import Database


def test_available_buns():
    database = Database()
    assert len(database.available_buns()) == 3


def test_available_ingredients():
    database = Database()
    assert len(database.available_ingredients()) == 6
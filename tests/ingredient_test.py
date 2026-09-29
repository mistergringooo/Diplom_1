from praktikum.ingredient import Ingredient


def test_get_name():
    ingredient = Ingredient('SAUCE', 'Соус', 50)
    assert ingredient.get_name() == 'Соус'


def test_get_price():
    ingredient = Ingredient('SAUCE', 'Соус', 50)
    assert ingredient.get_price() == 50


def test_get_type():
    ingredient = Ingredient('SAUCE', 'Соус', 50)
    assert ingredient.get_type() == 'SAUCE'
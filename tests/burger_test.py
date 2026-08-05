from unittest.mock import Mock
import pytest

from praktikum.burger import Burger


@pytest.mark.parametrize('bun_price, ingredient_price, expected', [
    (100, 50, 250),
    (200, 0, 400),
])
def test_get_price(bun_price, ingredient_price, expected):
    mock_bun = Mock()
    mock_bun.get_price.return_value = bun_price

    mock_ingredient = Mock()
    mock_ingredient.get_price.return_value = ingredient_price

    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)

    assert burger.get_price() == expected


def test_set_buns():
    burger = Burger()
    mock_bun = Mock()

    burger.set_buns(mock_bun)

    assert burger.bun == mock_bun

def test_add_ingredient():
    burger = Burger()
    mock_ingredient = Mock()

    burger.add_ingredient(mock_ingredient)

    assert len(burger.ingredients) == 1
    assert burger.ingredients[0] == mock_ingredient

def test_remove_ingredient():
    burger = Burger()
    mock_ingredient_1 = Mock()
    mock_ingredient_2 = Mock()

    burger.add_ingredient(mock_ingredient_1)
    burger.add_ingredient(mock_ingredient_2)

    burger.remove_ingredient(0)

    assert len(burger.ingredients) == 1
    assert burger.ingredients[0] == mock_ingredient_2

def test_move_ingredient():
    burger = Burger()
    mock_ingredient_1 = Mock()
    mock_ingredient_2 = Mock()
    mock_ingredient_3 = Mock()

    burger.add_ingredient(mock_ingredient_1)
    burger.add_ingredient(mock_ingredient_2)
    burger.add_ingredient(mock_ingredient_3)

    burger.move_ingredient(0, 2)

    assert burger.ingredients == [mock_ingredient_2, mock_ingredient_3, mock_ingredient_1]

def test_get_receipt():
    mock_bun = Mock()
    mock_bun.get_name.return_value = 'Космобулка'
    mock_bun.get_price.return_value = 100

    mock_ingredient = Mock()
    mock_ingredient.get_type.return_value = 'SAUCE'
    mock_ingredient.get_name.return_value = 'Соус'
    mock_ingredient.get_price.return_value = 50

    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)

    expected_receipt = (
        '(==== Космобулка ====)\n'
        '= sauce Соус =\n'
        '(==== Космобулка ====)\n'
        '\n'
        'Price: 250'
    )

    assert burger.get_receipt() == expected_receipt
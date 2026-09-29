from praktikum.bun import Bun


def test_get_name():
    bun = Bun('Космобулка', 100)
    assert bun.get_name() == 'Космобулка'


def test_get_price():
    bun = Bun('Космобулка', 100)
    assert bun.get_price() == 100
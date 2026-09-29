# Diplom_1 — Юнит-тесты сборки заказа Stellar Burgers

Юнит-тесты на pytest для классов, отвечающих за сборку заказа в Stellar Burgers. Дипломный проект курса «Тестировщик ПО с нуля» (Яндекс Практикум).

## Что проверяется

Классы модуля `praktikum`, отвечающие за бизнес-логику сборки бургера:

- **`Bun`** — булка бургера
- **`Burger`** — сборка бургера: добавление/удаление ингредиентов, подсчёт цены, получение чека
- **`Ingredient`** — ингредиент (тип + цена)
- **`Database`** — база доступных ингредиентов и булок

**14 тестов**, 100% покрытие этих четырёх классов (`bun_test.py`, `burger_test.py`, `database_test.py`, `ingredient_test.py`). Демонстрационный скрипт `praktikum.py` сознательно не покрывается тестами — по заданию курса проверке подлежит только бизнес-логика классов.

## Стек

Python, pytest, pytest-cov

## Структура проекта

```
praktikum/
├── __init__.py
├── bun.py                # класс Bun
├── burger.py              # класс Burger
├── database.py            # класс Database
├── ingredient.py           # класс Ingredient
├── ingredient_types.py       # перечисление типов ингредиентов
└── praktikum.py            # демонстрационный скрипт (не покрывается тестами)
tests/
├── bun_test.py
├── burger_test.py
├── database_test.py
└── ingredient_test.py
```

## Как запустить

```bash
pip install -r requirements.txt
pytest --cov=praktikum --cov-report=html
```

Отчёт о покрытии откроется в `htmlcov/index.html`.

import pytest
from pizza import (
    Margherita,
    Pepperoni,
    Hawaiian,
    PizzaMenu,
    bake,
    delivery,
    pickup,
)


# Тестирование классов пиццы
class TestPizzaClasses:
    def test_margherita_ingredients(self):
        margherita = Margherita()
        assert margherita.ingredients == [
            "tomato sauce",
            "mozzarella",
            "tomatoes",
        ]

    def test_pepperoni_ingredients(self):
        pepperoni = Pepperoni()
        assert pepperoni.ingredients == [
            "tomato sauce",
            "mozzarella",
            "pepperoni",
        ]

    def test_hawaiian_ingredients(self):
        hawaiian = Hawaiian()
        assert hawaiian.ingredients == [
            "tomato sauce",
            "mozzarella",
            "chicken",
            "pineapple",
        ]

    def test_pizza_equality(self):
        pizza1 = Margherita()
        pizza2 = Margherita()
        assert pizza1 == pizza2

        pizza3 = Pepperoni()
        assert pizza1 != pizza3

    def test_invalid_size(self):
        with pytest.raises(ValueError):
            Margherita("Medium")


# Тестирование меню
def test_pizza_menu():
    menu = PizzaMenu.menu()
    assert "Margherita" in menu
    assert "Pepperoni" in menu
    assert "Hawaiian" in menu


# Тестирование функций логгирования
class TestLoggingDecorators:
    def test_bake_logging(self, capsys):
        pizza = Margherita()
        bake(pizza)
        captured = capsys.readouterr()
        assert "Пицца 'Margherita' приготовлена" in captured.out

    def test_delivery_logging(self, capsys):
        delivery("Margherita")
        captured = capsys.readouterr()
        assert "Пицца 'Margherita' доставлена" in captured.out

    def test_pickup_logging(self, capsys):
        pickup("Margherita")
        captured = capsys.readouterr()
        assert "Пиццу 'Margherita' забрали" in captured.out

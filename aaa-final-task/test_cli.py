from click.testing import CliRunner
from cli import cli


# Тестирование вывода меню
def test_menu_output():
    runner = CliRunner()
    result = runner.invoke(cli, ["menu"])
    assert result.exit_code == 0
    assert "Margherita 🧀 size('L'/'XL')" in result.output
    assert "Pepperoni 🍕 size('L'/'XL')" in result.output
    assert "Hawaiian 🍍 size('L'/'XL')" in result.output


# Тестирование команды заказа с доставкой
def test_order_with_delivery():
    runner = CliRunner()
    result = runner.invoke(cli, ["order", "--courier", "Margherita", "L"])
    assert result.exit_code == 0
    assert "Готовим и доставляем 'Margherita' размер 'L'" in result.output
    assert "Пицца 'Margherita' доставлена" in result.output


# Тестирование команды заказа на самовывоз
def test_order_for_pickup():
    runner = CliRunner()
    result = runner.invoke(cli, ["order", "Pepperoni", "XL"])
    assert result.exit_code == 0
    assert "Готовим на самовывоз 'Pepperoni' размер 'XL'" in result.output
    assert "Пиццу 'Pepperoni' забрали" in result.output


# Тестирование обработки неверного названия пиццы
def test_order_invalid_pizza():
    runner = CliRunner()
    result = runner.invoke(cli, ["order", "S kolbaskoy", "L"])
    assert result.exit_code == 0
    assert (
        "Извините, пиццы с названием 'S kolbaskoy' нет в меню."
        in result.output
    )

import click
from pizza import (
    Margherita,
    Pepperoni,
    Hawaiian,
    PizzaMenu,
    bake,
    delivery,
    pickup,
)


@click.group()
def cli():
    pass


@cli.command()
@click.option("--courier", default=False, is_flag=True)
@click.argument("pizza")
@click.argument("size")
def order(pizza: str, size: str, courier: bool):
    """Готовит и доставляет пиццу"""
    pizza = pizza.capitalize()
    try:
        pizza_obj = {
            "Margherita": Margherita(size),
            "Pepperoni": Pepperoni(size),
            "Hawaiian": Hawaiian(size),
        }[pizza]

        if courier:
            print(
                f"Готовим и доставляем {pizza_obj.__class__.__name__!r} "
                f"размер {pizza_obj.size!r}"
            )
            bake(pizza_obj)
            delivery(pizza)
        else:
            print(
                f"Готовим на самовывоз {pizza_obj.__class__.__name__!r} "
                f"размер {pizza_obj.size!r}"
            )
            bake(pizza_obj)
            pickup(pizza)
    except KeyError:
        print(f"Извините, пиццы с названием {pizza!r} нет в меню.")


@cli.command()
def menu():
    """Выводит меню"""
    for name, (img, size, ingredients) in PizzaMenu.menu().items():
        print(
            f"- {name} {img} size({size[0]!r}/{size[1]!r}): "
            f"{', '.join(ingredients)}"
        )


if __name__ == "__main__":
    cli()

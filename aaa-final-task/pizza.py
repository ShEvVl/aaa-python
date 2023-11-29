import random
import time
from typing import Dict, List, Tuple


class Pizza:
    """`Pizza` Class.

    Methods:
    --------
        - `__init__`: parameter initialization;
        - `__eq__`: comparison;
        - `get_ingredients`: ingredient request.
    """

    ingredients: List[str] = []
    img: str = ""

    def __init__(self, size: str = "L") -> None:
        if size not in ("L", "XL"):
            raise ValueError("The size of the pizza should be 'L' or 'XL'")
        self.name = self.__class__.__name__
        self.size = size
        self.ingredients = self.__class__.ingredients
        self.img = self.__class__.img

    def __eq__(self, other) -> bool:
        """Compares two instances of a class:
            - By pizza name;
            - ingredients (sorted);
            - pizza size.

        Args:
        -----
            `other`: class
                another instance of the class

        Returns:
        --------
            `ans`: bool
                `True` - if all are equal,\n
                `False` - if at least one is not\n
                `NotImplemented` - if not an instance of Pizza.
        """
        if not isinstance(other, Pizza):
            return NotImplemented
        return (
            self.name == other.name
            and sorted(self.ingredients) == sorted(other.ingredients)
            and self.size == other.size
        )

    def get_ingredients(self) -> Dict[str, List[str]]:
        """Function for requesting pizza ingredients

        Returns:
        --------
            `ans`: Dict[str, List[str]]
                dictionary, where the key is the name of the pizza,
                value is the list of ingredients
        """
        return {self.name: self.ingredients}


class Margherita(Pizza):
    """`Margherita` class
        `pizza`(parent class)

    Ingredients:
    ------------
        - `tomato sauce`
        - `mozzarella`
        - `tomatoes`
    """

    ingredients = ["tomato sauce", "mozzarella", "tomatoes"]
    img = "🧀"


class Pepperoni(Pizza):
    """`Pepperoni` class.
        `pizza`(parent class)

    Ingredients:
    ------------
        - `tomato sauce`
        - `mozzarella`
        - `pepperoni`
    """

    ingredients = ["tomato sauce", "mozzarella", "pepperoni"]
    img = "🍕"


class Hawaiian(Pizza):
    """`Hawaiian` class.
        `pizza`(parent class)

    Ingredients:
    ------------
        - `tomato sauce`
        - `mozzarella`
        - `chicken`
        - `pineapple`
    """

    ingredients = ["tomato sauce", "mozzarella", "chicken", "pineapple"]
    img = "🍍"


class PizzaMenu:
    """Pizzeria Menu Class.

    Methods:
    --------
        - `menu` (`@staticmethod`) pizzeria menu request
    """

    @staticmethod
    def menu() -> Dict[str, Tuple[str, Tuple[str, str], List[str]]]:
        """Pizzeria menu.

        Returns:
        --------
            `ans`: Dict
                pizza name: (image, (size options), composition)
        """
        recipes = {
            "Margherita": (
                "🧀",
                ("L", "XL"),
                ["tomato sauce", "mozzarella", "tomatoes"],
            ),
            "Pepperoni": (
                "🍕",
                ("L", "XL"),
                ["tomato sauce", "mozzarella", "pepperoni"],
            ),
            "Hawaiian": (
                "🍍",
                ("L", "XL"),
                ["tomato sauce", "mozzarella", "chicken", "pineapple"],
            ),
        }
        return recipes


def log(message_template: str):
    """The function-decorator of the message envelope.

    Args:
    -----
        `message_template`: str
            custom message input
    """

    def decorator(func):
        """Decorator

        Args:
        -----
            `func`: func
                function transfer
        """

        def wrapper(*args, **kwargs):
            """Wrapper

            Returns:
            --------
                `result`:
                    function result
            """
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            message = f"{message_template} {elapsed_time:.0f} c!"
            print(message)
            return result

        return wrapper

    return decorator


@log("🧑‍🍳 Приготовили за")
def bake(pizza_obj: Pizza):
    """Готовит пиццу"""
    name, ingredients = list(pizza_obj.get_ingredients().items())[0]
    time.sleep(random.randint(2, 5))
    print(f"Пицца {name!r} приготовлена\n Состав: {', '.join(ingredients)}")


@log("🛵 Доставили за")
def delivery(pizza: str):
    """Доставляет пиццу"""
    time.sleep(random.randint(2, 5))
    print(f"Пицца {pizza!r} доставлена")


@log("🏠 Забрали за")
def pickup(pizza: str):
    """Самовывоз"""
    time.sleep(random.randint(2, 5))
    print(f"Пиццу {pizza!r} забрали")

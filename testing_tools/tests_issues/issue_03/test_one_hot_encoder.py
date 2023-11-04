import unittest
from .one_hot_encoder import fit_transform


class TestFitTransform(unittest.TestCase):
    def test_cities(self):
        cities = ["Moscow", "New York", "Moscow", "London"]
        exp_transformed_cities = [
            ("Moscow", [0, 0, 1]),
            ("New York", [0, 1, 0]),
            ("Moscow", [0, 0, 1]),
            ("London", [1, 0, 0]),
        ]
        self.assertEqual(fit_transform(cities), exp_transformed_cities)

    def test_empty(self):
        with self.assertRaises(TypeError):
            fit_transform()

    def test_uniqueness(self):
        inputs = ["a", "b", "c", "a"]
        output = fit_transform(inputs)
        unique_codes = {tuple(item[1]) for item in output}
        self.assertEqual(len(unique_codes), len(set(inputs)))

    def test_non_inclusion_multiple(self):
        categories = ["apple", "banana", "cherry", "apple"]
        not_in_categories = ["pineapple", "mango", "grape"]
        transformed = fit_transform(categories)
        transformed_categories = [item[0] for item in transformed]
        for category in not_in_categories:
            self.assertNotIn(category, transformed_categories)

    def test_non_inclusion_empty_input(self):
        categories = []
        not_in_categories = "void"
        transformed = fit_transform(categories)
        transformed_categories = [item[0] for item in transformed]
        self.assertNotIn(not_in_categories, transformed_categories)

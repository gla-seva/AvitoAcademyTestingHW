from one_hot_encoder import fit_transform
import unittest


class TestOneHotEncode(unittest.TestCase):
    def test_list(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        transformed_cities = fit_transform(cities)
        self.assertEqual(transformed_cities, exp_transformed_cities)

    def test_empty_list(self):
        cities = []
        exp_transformed_cities = []
        transformed_cities = fit_transform(cities)
        self.assertEqual(transformed_cities, exp_transformed_cities)

    def test_empty_str(self):
        with self.assertRaises(TypeError):
            fit_transform()

    def test_str(self):
        cities = 'ab'
        exp_transformed_cities = [
            ('a', [0, 1]),
            ('b', [1, 0]),
        ]
        transformed_cities = fit_transform(*cities)
        self.assertEqual(transformed_cities, exp_transformed_cities)

    def test_wrong_str(self):
        cities = 'ab'
        exp_transformed_cities = [
            ('a', [0, 1]),
            ('b', [0, 1]),
        ]
        transformed_cities = fit_transform(*cities)
        self.assertNotEqual(transformed_cities, exp_transformed_cities)

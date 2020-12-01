from one_hot_encoder import fit_transform
import pytest


def test_list():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    transformed_cities = fit_transform(cities)
    assert transformed_cities == exp_transformed_cities


def test_empty_list():
    cities = []
    exp_transformed_cities = []
    transformed_cities = fit_transform(cities)
    assert transformed_cities == exp_transformed_cities


def test_empty_str():
    with pytest.raises(TypeError):
        fit_transform()


def test_str():
    cities = 'ab'
    exp_transformed_cities = [
        ('a', [0, 1]),
        ('b', [1, 0]),
    ]
    transformed_cities = fit_transform(*cities)
    assert transformed_cities == exp_transformed_cities


def test_wrong_str():
    cities = 'ab'
    exp_transformed_cities = [
        ('a', [0, 1]),
        ('b', [0, 1]),
    ]
    transformed_cities = fit_transform(*cities)
    assert transformed_cities != exp_transformed_cities

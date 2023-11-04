import pytest
from one_hot_encoder import fit_transform


def test_single_argument():
    expected = [("Moscow", [1])]
    result = fit_transform("Moscow")
    assert result == expected


def test_multiple_arguments():
    expected = [
        ("Moscow", [0, 0, 1]),
        ("New York", [0, 1, 0]),
        ("London", [1, 0, 0]),
    ]
    result = fit_transform("Moscow", "New York", "London")
    assert result == expected


def test_repeated_arguments():
    expected = [("Moscow", [1]), ("Moscow", [1])]
    result = fit_transform("Moscow", "Moscow")
    assert result == expected


def test_no_arguments():
    with pytest.raises(TypeError):
        fit_transform()


def test_empty_string_argument():
    expected = [("", [1])]
    result = fit_transform("")
    assert result == expected


def test_numerical_argument():
    with pytest.raises(TypeError):
        fit_transform(123)

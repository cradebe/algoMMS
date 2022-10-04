import pytest

from algorithm import find_number


@pytest.fixture
def short_array():
    array = [3, 4, 6, 9, 10, 12, 14, 15, 17, 19, 21]
    yield array


@pytest.fixture
def long_array():
    array_long = list(range(5, 5000, 2))
    yield array_long


def test_find_number_target_in_array(short_array):
    assert find_number(short_array, 12) == 12


def test_find_number_target_not_in_array(short_array):
    assert find_number(short_array, 7) == 6


def test_find_number_target_string(short_array):
    assert find_number(short_array, 'Nine') == -1


def test_find_number_target_greater_than_array_max(short_array):
    assert find_number(short_array, 500) == 21


def test_find_number_target_less_than_array_min(short_array):
    assert find_number(short_array, 1) == -1


def test_find_number_target_long_array_target_not_in_array(long_array):
    assert find_number(long_array, 50) == 49

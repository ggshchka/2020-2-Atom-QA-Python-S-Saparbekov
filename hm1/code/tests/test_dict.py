"""
Tests for string
"""
from contextlib import nullcontext as does_not_raise
import pytest


class TestDictStruct:
    """
    TestDictStruct
    """

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            ({}, pytest.raises(KeyError)),
            ({'key1': 1, 'key2': 2}, does_not_raise()),
            ({'key0': 1, 'key2': None}, pytest.raises(KeyError)),
        ],
    )
    def test_dict_pop_error(self, test_input, expected):
        """ №1 """
        with expected:
            assert test_input.pop('key1') is not None


    def test_dict_all(self):
        """ №2 """
        assert all({1: False, True: True, 1.0: None})


    @pytest.mark.parametrize(
        "test_input, expected",
        [
            ({}, {}),
            ({'key1': 1, 'key2': 2}, {'key1': 1, 'key2': 2}),
            ({'key2': 2, 'key1': 1}, {'key1': 1, 'key2': 2}),
        ],
    )
    def test_dict_comparison(self, test_input, expected):
        """ №3 """
        assert test_input == expected


    def test_dict_with_same_keys(self):
        """ №4 """
        assert {'key1': 5, 'key2': False, 'key1': None} == {'key2': False, 'key1': None}

    def test_dict_clear(self, rand_dict):
        """ №5 """
        rand_dict.clear()
        assert len(rand_dict) == 0

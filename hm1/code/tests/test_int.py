"""
Tests for integer
"""
import math
import pytest


class TestIntStruct:
    """
        Test of integer class
    """

    @pytest.mark.parametrize("test_input, expected",
        [
            (15, 225),
            (-20, 400),
            (0, 0),
            (-1, 1),
            (1, 1),
        ],
    )
    def test_int_quad(self, test_input, expected):
        """
        №1.
        """
        assert test_input**2 == expected


    def test_int_sqrt_assert(self):
        """
        №2.
        """
        a = -9
        with pytest.raises(ValueError):
            assert math.sqrt(a)


    def test_int_is_instance(self, rand_int):
        """
        №3.
        """
        assert isinstance(rand_int, int)


    @pytest.mark.parametrize(
        "test_input, expected",
        [
            (3.5, 3),
            (-0.43, 0),
            ('3', 3),
            #(('12', 8), 10),
            (0o10, 8),
        ],
    )
    def test_int_func_to_int(self, test_input, expected):
        """
        №4.
        """
        assert int(test_input) == expected


    @pytest.mark.parametrize(
        "input_x, input_y, expected",
        [
            (0, 1, 0),
            (-1, 2, -1),
            (1, -2, -1),
            (1, 2, 0),
            (-1, -2, 0),
        ],
    )
    def test_int_div(self, input_x, input_y, expected):
        """
        №5.
        """
        assert input_x // input_y == expected

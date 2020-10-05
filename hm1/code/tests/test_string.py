"""
Tests for string
"""
import pytest


def test_string_len_concat(rand_2_strings):
    """
    №1.
    Check that the length of concatenation strings is equal to
    sum of the lengths of each string
    """
    str1, str2 = rand_2_strings
    assert len(str1 + str2) == len(str1) + len(str2)


class TestStringStruct:
    """
        Test of string class
    """

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            ("i see a red door", "I SEE A RED DOOR"),
            ("And I Want It painTed blAck", "AND I WANT IT PAINTED BLACK"),
            ("NO COLORS ANYMORE,", "NO COLORS ANYMORE,"),
            ("", ""),
            ("4head", "4HEAD")
        ],
    )
    def test_string_is_upper(self, test_input, expected):
        """ №2 """
        assert test_input.upper() == expected


    def test_string_strip_error(self):
        """ №3 """
        text = "I want them to turn black"
        with pytest.raises(TypeError) as excinfo:
            text.strip(5)
        assert "strip arg must be None or str" in str(excinfo.value)


    def test_string_rjust(self):
        """ №4 """
        str_ = "Joke"
        fill = "$"
        assert str_.rjust(5, fill) == "$Joke"


    def test_string_find(self):
        """ №5 """
        str_ = 'Let it be, let it be, let it be'
        assert str_.find("let it be") == 11

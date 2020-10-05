import pytest

class TestSetStruct:
    """
    TestSetStruct
    """


    def test_set_equal(self):
        """ №1 """
        assert {None, True, 4} == {None, 4, True} \
               == {True, None, 4} == {True, 4, None} \
               == {4, True, None} == {4, None, True} \


    def test_empty_set_type(self):
        """ №2 """
        s = set()
        d = {}
        assert isinstance(s, set) and not isinstance(d, set)


    @pytest.mark.parametrize(
        "set_x, set_y, res",
        [
            ({0, False, None}, set(), {0, False, None}),
            (set(), set(), set()),
            ({-5, 4, True, None}, {"-5", None, 4.0}, {-5, 4, True, None, "-5"})
        ]
    )
    def test_set_union(self, set_x, set_y, res):
        """ №3 """
        assert set_x.union(set_y) == res


    @pytest.mark.parametrize(
        "set_x, set_y, res",
        [
            ({0, False, None}, set(), set()),
            (set(), set(), set()),
            ({-5, 4, True, None}, {"-5", None, 4.0}, {None, 4})
        ]
    )
    def test_set_intersection(self, set_x, set_y, res):
        """ №4 """
        assert set_x.intersection(set_y) == res


    @pytest.mark.parametrize(
        "set_x, set_y, res",
        [
            ({0, False, None}, set(), {0, False, None}),
            (set(), {0, False, None}, set()),
            (set(), set(), set()),
            ({-5, 4, True, None}, {"-5", None, 4.0}, {True, -5})
        ]
    )
    def test_set_diff(self, set_x, set_y, res):
        """ №5 """
        assert set_x - set_y == res
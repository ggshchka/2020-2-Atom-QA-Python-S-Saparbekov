import pytest

class TestListStruct:


    def test_list_len_after_append(self, rand_list):
        """ №1 """
        l = len(rand_list)
        rand_list.append("new element")
        assert len(rand_list) == l + 1


    @pytest.mark.parametrize(
        "input, expected",
        [
            ([1, 'two', 'a', 4], [4, 'a', 'two', 1]),
            ([], []),
            ([0], [0]),
            ([None], [None]),
        ]
    )
    def test_list_reverse(self, input, expected):
        """ №2 """
        input.reverse()
        assert input == expected


    def test_list_sort_diff_instances(self):
        """ №3 """
        with pytest.raises(TypeError):
            assert [4,"0", "AbC", None].sort()


    def test_list_index_error_raises(self):
        """ №4 """
        with pytest.raises(ValueError) as exc:
            [2,"12",None,[1,4],(5,3),4.3,True].index(4.31)
        assert "is not in list" in str(exc.value)


    def test_list_clear(self, rand_list):
        """ №5 """
        rand_list.clear()
        assert len(rand_list) == 0

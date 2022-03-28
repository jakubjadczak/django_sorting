from algorithms.utils import get_random_text, sort_custom_seq, sort
from alg_codes.numbers_gen import DataGenerator
from alg_codes.sorting_algs import shell_sort, quick_sort


class TestUtils:

    def test_random_text(self):
        text1 = get_random_text()
        text2 = get_random_text()

        assert text1 != text2

    def test_custom_seq(self):
        dg = DataGenerator()
        v = '1 3 45 23 67 54 0'

        result = sort_custom_seq(v, shell_sort)
        sorted_list = result[0]
        comp = result[1]
        swap = result[2]
        temp = result[3]
        time = result[4]

        assert isinstance(sorted_list, list)
        assert isinstance(comp, int)
        assert isinstance(swap, int)
        assert isinstance(temp, list)
        assert isinstance(time, float)

    def test_random_seq(self):
        result = sort('A', 15, quick_sort)
        time = result[0]
        comp = result[1]
        swap = result[2]

        assert isinstance(time, float)
        assert isinstance(comp, int)
        assert isinstance(swap, int)
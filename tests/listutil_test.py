import unittest

from listutil import count_unique
from listutil import binary_search


class TestUnique(unittest.TestCase):

    def test_one_unique(self):
        list = [1]
        self.assertEquals(1, count_unique(list))

    def test_two_unique(self):
        list = ['a', 'b', 'a', 'b']
        self.assertEquals(2, count_unique(list))

    def test_empty(self):
        list = []
        self.assertEquals(0, count_unique(list))

    def test_three_unique(self):
        list = ['a', 'c', 'b', 'b', 'b', 'a', 'c', 'c']
        self.assertEquals(3, count_unique(list))

    def test_upper_and_lower(self):
        list = ['a', 'A']
        self.assertEquals(3, count_unique(list))

    def test_two_upper_and_lower(self):
        list = ['a', 'A', 'b', 'B']
        self.assertEquals(3, count_unique(list))


class TestBinary(unittest.TestCase):

    def test_nine_lenght(self):
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(4, binary_search(list, 5))

    def test_triple_one(self):
        list = [1, 1, 1]
        self.assertEqual(1, binary_search(list, 1))

    def test_out_of_range(self):
        list = [0, 1, 2, 3, 4]
        self.assertEquals(-1, binary_search(list, 5))

    def test_none(self):
        list = None
        self.assertRaises(TypeError)

    def test_empty_list(self):
        list = []
        self.assertEquals(-1, binary_search(list, ""))


if __name__ == "__main__":
    unittest.main()
import unittest

from listutil import count_unique


class tester(unittest.TestCase):

    def test_one_unique(self):
        list = [1]
        self.assertEquals(1, count_unique(list))

    def test_two_unique(self):
        list = ['a', 'b', 'a', 'b']
        self.assertEquals(2, count_unique(list))

    def test_empty(self):
        list = []
        self.assertEquals(0, count_unique(list))

    def test_none(self):
        list = 10
        self.assertEquals(, count_unique())
import unittest

from leetcode10 import Solution


class TestLeetcode10(unittest.TestCase):
    def test_len1_9(self):
        self.assertEqual(Solution.plus_one([9]), [1, 0], 'Должно получиться [1, 0]')

    def test_9(self):
        self.assertEqual(Solution.plus_one([1, 2, 9]), [1, 3, 0], 'Должно получиться [1, 3, 0]')

    def test_99(self):
        self.assertEqual(Solution.plus_one([9, 9]), [1, 0, 0], 'Должно получиться [1, 0, 0]')





import unittest

from leetcode11 import Solution


class TestLeetcode10(unittest.TestCase):
    def test_(self):
        self.assertEqual(Solution.length_of_last_word('Hello world'), 5, 'Должно получиться 5')

    def test_spaces(self):
        self.assertEqual(Solution.length_of_last_word('Hello world  '), 5, 'Должно получиться 5')

    def test_len_1(self):
        self.assertEqual(Solution.length_of_last_word(' w'), 1, 'Должно получиться 1')

import unittest

from leetcode12 import Solution


class TestLeetcode12(unittest.TestCase):
    def test_type_result(self):
        self.assertIsInstance(Solution.add_binary('10', '10'), str, 'Возвращает str')

    def test_different_len(self):
        self.assertEqual(Solution.add_binary('101', '10'), '111', 'Корректно складывает строки разной длины')

    def test_expansion_len(self):
        self.assertEqual(Solution.add_binary('101', '101'), '1010', 'В случае необходимости увеличивает длину')
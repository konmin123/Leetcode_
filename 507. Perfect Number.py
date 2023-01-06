"""A perfect number is a positive integer that is equal to the sum of its
positive divisors, excluding the number itself. A divisor of an integer x is an
integer that can divide x evenly.

Given an integer n, return true if n is a perfect number, otherwise return
false.

Example 1:
Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.

Example 2:
Input: num = 7
Output: false

Constraints:
1 <= num <= 108"""


class Solution:
    @staticmethod
    def check_perfect_number(num: int) -> bool:
        list_divisor = []
        for divisor in range(1, num // 2 + 1):
            if num % divisor == 0:
                list_divisor.append(divisor)
        return sum(list_divisor) == num

    @staticmethod
    def check_perfect_number_comp(num: int) -> bool:
        list_divisor = [x for x in range(1, num // 2 + 1) if num % x == 0]
        return sum(list_divisor) == num


assert Solution.check_perfect_number(28) is True
assert Solution.check_perfect_number(7) is False
assert Solution.check_perfect_number_comp(28) is True
assert Solution.check_perfect_number_comp(7) is False

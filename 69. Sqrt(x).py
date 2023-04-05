"""Given a non-negative integer x, return the square root of x rounded down to
the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to
the nearest integer, 2 is returned.

Constraints:
0 <= x <= 231 - 1"""
from math import sqrt


class Solution:
    @staticmethod
    def my_sqrt(x: int) -> int:
        return int(sqrt(x))

    @staticmethod
    def my_sqrt_binary_find(x: int) -> int:
        left = 1
        right = x
        while left <= right:
            middle = (right + left) // 2
            if middle ** 2 < x:
                if (middle + 1) ** 2 > x:
                    return middle
                left = middle + 1
            elif middle ** 2 > x:
                right = middle - 1
            else:
                return middle


assert Solution.my_sqrt_binary_find(9) == 3
assert Solution.my_sqrt_binary_find(8) == 2
assert Solution.my_sqrt_binary_find(30) == 5
assert Solution.my_sqrt_binary_find(626) == 25

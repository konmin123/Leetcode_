"""
Given a signed 32-bit integer x, return x with its digits reversed. If
reversing x causes the value to go outside the signed 32-bit integer range
[-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or
unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21


Constraints:

-231 <= x <= 231 - 1
"""


class Solution:
    @staticmethod
    def reverse(x: int) -> int:
        if abs(x) > 2147483647:
            return 0
        output = ''
        for number in str(abs(x))[::-1]:
            output = output + number
        return int(output) if x > 0 else -int(output)


assert Solution.reverse(123) == 321
assert Solution.reverse(-123) == -321

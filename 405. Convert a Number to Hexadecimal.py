"""Given an integer num, return a string representing its hexadecimal
representation. For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters, and there
should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve
this problem.

Example 1:
Input: num = 26
Output: "1a"

Example 2:
Input: num = -1
Output: "ffffffff"

Constraints:
-231 <= num <= 231 - 1"""


class Solution:
    @staticmethod
    def to_hex(num: int) -> str:
        values_for_repr = {10: 'a',
                           11: 'b',
                           12: 'c',
                           13: 'd',
                           14: 'e',
                           15: 'f'}
        output = ''
        remainder = num
        if num < 0:
            remainder = num + 2 ** 32
        elif num == 0:
            return '0'
        while remainder > 0:
            if remainder % 16 == 0:
                output = '1' + output
            elif remainder % 16 < 10:
                output = str(remainder % 16) + output
            elif remainder % 16 >= 10:
                output = values_for_repr[remainder % 16] + output
            remainder = remainder // 16
        return output


print(Solution.to_hex(1515))
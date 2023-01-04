"""Given an integer num, return a string of its base 7 representation.

Example 1:
Input: num = 100
Output: "202"

Example 2:
Input: num = -7
Output: "-10"

Constraints:
-107 <= num <= 107"""


class Solution:
    @staticmethod
    def convert_to_base_7(num: int) -> str:
        prefix = '' if num > 0 else '-'
        output = str(abs(num) % 7)
        integer_part = abs(num) // 7
        while integer_part > 7:
            output = str(integer_part % 7) + output
            integer_part = integer_part // 7
        output = str(integer_part) + output
        return prefix + output


assert Solution.convert_to_base_7(-7) == '-10'
assert Solution.convert_to_base_7(10) == '13'
assert Solution.convert_to_base_7(-100) == '-202'

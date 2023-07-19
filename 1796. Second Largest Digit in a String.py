"""
Given an alphanumeric string s, return the second largest numerical digit that
appears in s, or -1 if it does not exist. An alphanumeric string is a string
consisting of lowercase English letters and digits.

Example 1:
Input: s = "dfa12321afd"
Output: 2
Explanation: The digits that appear in s are [1, 2, 3]. The second largest
digit is 2.

Example 2:
Input: s = "abc1111"
Output: -1
Explanation: The digits that appear in s are [1]. There is no second largest
digit.

Constraints:
1 <= s.length <= 500
s consists of only lowercase English letters and/or digits.
"""


class Solution:
    @staticmethod
    def second_highest(s: str) -> int:
        largest_digit: int = -1
        second_largest_digit: int = -1
        for item in s:
            if item.isdigit():
                item = int(item)
                if item > largest_digit:
                    largest_digit, second_largest_digit = item, largest_digit
                elif largest_digit > item > second_largest_digit:
                    second_largest_digit = item
        return second_largest_digit


assert Solution.second_highest("dfa12321afd") == 2
assert Solution.second_highest("abc1111") == -1

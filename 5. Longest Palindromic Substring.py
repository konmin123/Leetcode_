"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""


class Solution:
    @staticmethod
    def longest_palindrome(s: str) -> str:
        for len_temp in range(len(s), 1, -1):
            left_border: int = 0
            right_border: int = left_border + len_temp
            while right_border <= len(s):
                palindrome: str = s[left_border:right_border]
                if palindrome == palindrome[::-1]:
                    return palindrome
                left_border += 1
                right_border += 1
        return s[0]


assert Solution.longest_palindrome("babad") == "bab"
assert Solution.longest_palindrome("cbbd") == "bb"

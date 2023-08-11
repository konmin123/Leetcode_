"""
Given a string s, find the length of the longest substring without repeating
characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a
substring.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    @staticmethod
    def length_of_longest_substring(s: str) -> int:
        max_len = 0
        sub_str = set()
        for letter in s:
            if letter in sub_str:
                if len(sub_str) > max_len:
                    max_len = len(sub_str)
                sub_str = set()
            sub_str.add(letter)
        return max_len


assert Solution.length_of_longest_substring("abcabcbb") == 3
assert Solution.length_of_longest_substring("bbbbb") == 1
assert Solution.length_of_longest_substring("pwwkew") == 3

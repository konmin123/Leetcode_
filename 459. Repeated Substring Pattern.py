"""Given a string s, check if it can be constructed by taking a substring of
it and appending multiple copies of the substring together.

Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
Input: s = "aba"
Output: false

Example 3:
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc"
twice.

Constraints:
1 <= s.length <= 104
s consists of lowercase English letters."""
from collections import defaultdict


class Solution:
    @staticmethod
    def repeated_substring_pattern(s: str) -> bool:
        for index in range(len(s)):
            substring = s[:index]
            if s.count(substring) * len(substring) == len(s):
                return True
        return False

    @staticmethod
    def repeated_substring_pattern_dict(s: str) -> bool:
        dict_letters = defaultdict(int)
        for letter in s:
            dict_letters[letter] += 1
        set_dict_values = set(dict_letters.values())
        if len(set_dict_values) == 1:
            return True
        return False


print(Solution.repeated_substring_pattern_dict("abcabcabcabc"))
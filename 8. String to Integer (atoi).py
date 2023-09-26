"""
Given an input string s and a pattern p, implement regular expression matching
with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).



Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore,
by repeating 'a' once, it becomes "aa".

Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Constraints:
1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a
previous valid character to match.
"""


class Solution:
    @staticmethod
    def is_match(s: str, p: str) -> bool:
        if len(s) != len(p):
            return False
        for index in range(len(s)):
            if s[index] != p[index]:
                if p[index] == '*' and s[index] < s[index - 1]:
                    if p[index] != 0:
                        return False
        return True


assert not Solution.is_match('aa', 'a')
assert Solution.is_match('ab', 'a*')
assert Solution.is_match('ab', '.*')
assert Solution.is_match('abba', 'abba')
assert Solution.is_match('aaab', 'a..*')
assert Solution.is_match('', '')

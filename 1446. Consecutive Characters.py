"""The power of the string is the maximum length of a non-empty substring that
contains only one unique character. Given a string s, return the power of s.

Example 1:
Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

Constraints:
1 <= s.length <= 500
s consists of only lowercase English letters."""


class Solution:
    @staticmethod
    def max_power(s: str) -> int:
        output: int = 1
        together: int = 1
        prev: str = s[0]
        for letter in s[1:]:
            if letter == prev:
                together += 1
                output = max(output, together)
            else:
                together = 1
                prev = letter
        return output


assert Solution.max_power("leetcode") == 2
assert Solution.max_power("abbcccddddeeeeedcba") == 5
assert Solution.max_power("a") == 1

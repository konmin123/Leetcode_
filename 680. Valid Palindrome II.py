"""Given a string s, return true if the s can be palindrome after deleting at
most one character from it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false

Constraints:
1 <= s.length <= 105
s consists of lowercase English letters."""


class Solution:
    @staticmethod
    def valid_palindrome(s: str) -> bool:
        cur_r: int = -1
        wrong: int = 0
        for cur_l in range(len(s)//2 + 1):
            if s[cur_l] != s[cur_r]:
                wrong += 1
                if wrong > 1:
                    return False
            else:
                cur_r -= 1
        return True


assert Solution.valid_palindrome("aba")
assert Solution.valid_palindrome("abca")
assert not Solution.valid_palindrome("abc")

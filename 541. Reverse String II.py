"""Given a string s and an integer k, reverse the first k characters for every
2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are
less than 2k but greater than or equal to k characters, then reverse the first
k characters and leave the other as original.

Example 1:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Example 2:
Input: s = "abcd", k = 2
Output: "bacd"

Constraints:
1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 104"""


class Solution:
    @staticmethod
    def reverse_str(s: str, k: int) -> str:
        output: str = ''
        left_cur: int = 0
        count: int = 1
        for right_cur in range(k-1, len(s) - 1, k):
            part = s[left_cur:right_cur + 1]
            if count % 2 != 0:
                output += part[::-1]
            else:
                output += part
            left_cur = right_cur + 1
            count += 1
        output += s[left_cur:]
        return output


assert Solution.reverse_str("abcdefg", k=2) == "bacdfeg"
assert Solution.reverse_str("abcd", k=2) == "bacd"





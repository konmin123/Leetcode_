"""Given a binary string s, return the number of non-empty substrings that have
the same number of 0's and 1's, and all the 0's and all the 1's in these
substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they
occur.

Example 1:
Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's
and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times
they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not
grouped together.

Example 2:
Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal
number of consecutive 1's and 0's.

Constraints:
1 <= s.length <= 105
s[i] is either '0' or '1'."""


class Solution:
    @staticmethod
    def count_binary_substrings(s: str) -> int:
        len_patt: int = s.count('1')
        patterns: list = []
        output: int = 0
        for len_1 in range(len_patt, 0, -1):
            if ('1' * len_1) in s and ('0' * len_1) in s:
                break
        for len_ in range(1, len_patt + 1):
            patterns.append('1' * len_ + '0' * len_)
            patterns.append('0' * len_ + '1' * len_)
        for pattern in patterns:
            for index in range(len(s)):
                if pattern in s[index: len(pattern) + index:]:
                    output += 1
        return output


assert Solution.count_binary_substrings("00110011") == 6
assert Solution.count_binary_substrings("10101") == 4

"""Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Constraints:
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself."""


class Solution:
    @staticmethod
    def add_binary(a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        return f'{a + b:b}'


assert Solution.add_binary('11', '1') == '100'
assert Solution.add_binary('1010', '1011') == '10101'

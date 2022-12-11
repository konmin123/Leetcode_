"""Write a function that reverses a string. The input string is given as an
array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character."""
from typing import List


class Solution:
    @staticmethod
    def reverse_string(s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        first_cur = 0
        second_cur = len(s) - 1
        while first_cur < second_cur:
            s[first_cur], s[second_cur] = s[second_cur], s[first_cur]
            first_cur += 1
            second_cur -= 1
        print(s)

    @staticmethod
    def reverse_string_slice(s: List[str]) -> None:
        s = s[::-1]


s = ["H", "a", "n", "n", "a", "h"]

print(s)

Solution.reverse_string_slice(s)

print(s)

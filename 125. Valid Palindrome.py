"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and
numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:

    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.
"""


class Solution:
    @staticmethod
    def is_palindrome(s: str) -> bool:
        # left_str = " "
        # right_str = " "
        # for index in range(len(s)):
        #     if s[index].isalpha():
        #         left_str = left_str + s[index].lower()
        #     if s[-1 - index].isalpha():
        #         right_str = right_str + s[-1 - index].lower()
        # if left_str == right_str:
        #     return True
        # else:
        #     return False
        s = ''.join(c.lower() for c in s if c.isalnum())
        return s == s[::-1]


if __name__ == '__main__':
    print(Solution.is_palindrome("A man, a plan, a canal: Panama"))
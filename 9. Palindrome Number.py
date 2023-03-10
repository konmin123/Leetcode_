"""Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes
121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
-231 <= x <= 231 - 1
Follow up: Could you solve it without converting the integer to a string?"""


class Solution:
    @staticmethod
    def is_palindrome_str(x: int) -> bool:
        string: str = str(x)
        for index in range(len(string)):
            if string[index] != string[(-1 - index)]:
                return False
        return True

    @staticmethod
    def is_palindrome(x: int) -> bool:
        if x < 0:
            return False
        list_values = []
        while x >= 10:
            remains = x % 10
            x -= remains
            x /= 10
            list_values.append(int(remains))
        list_values.append(int(x))
        return list_values == list_values[::-1]


assert Solution.is_palindrome(121)
assert not Solution.is_palindrome(-121)
assert not Solution.is_palindrome(10)

"""Given a positive integer num, write a function which returns True if num is
a perfect square else False.
Follow up:
9

Example 1:
Input: num = 16
Output: true

Example 2:
Input: num = 14
Output: false

Constraints:
1 <= num <= 2^31 - 1"""


class Solution:
    @staticmethod
    def is_perfect_square_binary(num: int) -> bool:
        left = 1
        right = num
        while left <= right:
            middle = int((left + right) / 2)
            if middle ** 2 > num:
                right = middle - 1
            elif middle ** 2 < num:
                left = middle + 1
            else:
                return True
        return False


print(Solution.is_perfect_square_binary(4294967296))

"""Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.
Example 2:
Input: num = 0
Output: 0
Constraints:
    0 <= num <= 231 - 1
Follow up: Could you do it without any loop/recursion in O(1) runtime?
"""


class Solution:
    @staticmethod
    def sum_digits_while(num: int) -> int:
        output = num
        while len(str(output)) > 1:
            output = sum(map(int, str(output)))
        return output

    @staticmethod
    def best_sum_digits(num):
        return 0 if num == 0 else (num - 1) % 9 + 1


if __name__ == '__main__':
    print(Solution.best_sum_digits(40))
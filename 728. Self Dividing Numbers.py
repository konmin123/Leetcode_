"""A self-dividing number is a number that is divisible by every digit it
contains. For example, 128 is a self-dividing number because 128 % 1 == 0,
128 % 2 == 0, and 128 % 8 == 0. A self-dividing number is not allowed to
contain the digit zero. Given two integers left and right, return a list of all
the self-dividing numbers in the range [left, right].

Example 1:
Input: left = 1, right = 22
Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]

Example 2:
Input: left = 47, right = 85
Output: [48,55,66,77]

Constraints:
1 <= left <= right <= 104"""
from typing import List


class Solution:
    @staticmethod
    def self_dividing_numbers_bf(left: int, right: int) -> List[int]:
        output: List = []
        for number in range(left, right + 1):
            flag = True
            for element in str(number):
                if element == '0' or number % int(element):
                    flag = False
                    break
            if flag:
                output.append(number)
        return output


assert Solution.self_dividing_numbers_bf(1, 22) == [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22
]
assert Solution.self_dividing_numbers_bf(47, 85) == [48, 55, 66, 77]


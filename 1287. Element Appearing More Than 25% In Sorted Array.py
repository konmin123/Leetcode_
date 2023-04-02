"""Given an integer array sorted in non-decreasing order, there is exactly one
integer in the array that occurs more than 25% of the time, return that
integer.

Example 1:
Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6

Example 2:
Input: arr = [1,1]
Output: 1

Constraints:
1 <= arr.length <= 104
0 <= arr[i] <= 105"""
from typing import List


class Solution:
    @staticmethod
    def find_special_integer(arr: List[int]) -> int:
        return max(arr, key=lambda x: arr.count(x))


assert Solution.find_special_integer([1, 2, 2, 6, 6, 6, 6, 7, 10]) == 6
assert Solution.find_special_integer([1, 1]) == 1
assert Solution.find_special_integer([1]) == 1

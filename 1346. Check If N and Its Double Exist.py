"""Given an array arr of integers, check if there exist two indices i and j
such that :
i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]

Example 1:
Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

Example 2:
Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.

Constraints:
2 <= arr.length <= 500
-103 <= arr[i] <= 103"""
from typing import List


class Solution:
    @staticmethod
    def check_if_exist(arr: List[int]) -> bool:
        even_numbers: set = set()
        odd_numbers: set = set()
        for number in arr:
            if number % 2 == 0:
                even_numbers.add(number)
            else:
                odd_numbers.add(number)
        for odd_number in odd_numbers:
            if odd_number * 2 in even_numbers:
                return True
        return False


assert Solution.check_if_exist([10, 2, 5, 3])
assert not Solution.check_if_exist([3, 1, 7, 11])

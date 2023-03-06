"""Given an array of integers arr, return true if and only if it is a valid
mountain array. Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:
Input: arr = [2,1]
Output: false

Example 2:
Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true

Constraints:
1 <= arr.length <= 104
0 <= arr[i] <= 104"""
from typing import List


class Solution:
    @staticmethod
    def valid_mountain_array(arr: List[int]) -> bool:
        left_cur = 1
        right_cur = len(arr) - 1
        prev_left = arr[0]
        prev_right = arr[-1]
        while left_cur < right_cur:
            if arr[left_cur] >= prev_left and arr[right_cur] >= prev_right:
                prev_left = arr[left_cur]
                prev_right = arr[right_cur]
                left_cur += 1
                right_cur -= 1
            else:
                return False
        return True


assert Solution.valid_mountain_array([0, 3, 2, 1])
"""
Given an array nums with n objects colored red, white, or blue, sort them
in-place so that objects of the same color are adjacent, with the colors in
the order red, white, and blue. We will use the integers 0, 1, and 2 to
represent the color red, white, and blue, respectively. You must solve this
problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.

Could you come up with a one-pass algorithm using only constant extra space?
"""
from typing import List


class Solution:
    @staticmethod
    def sort_colors(nums: List[int]) -> None:
        dict_count = {'0': 0, '1': 0, '2': 0}
        for num in nums:
            dict_count[str(num)] += 1
        cur_color = 0
        for index, num in enumerate(nums):
            if dict_count[str(cur_color)] == 0:
                cur_color += 1
            nums[index] = cur_color
            dict_count[str(cur_color)] -= 1

    @staticmethod
    def sort_colors_best(arr: List[int]) -> None:
        border_l = 0
        border_r = len(arr) - 1
        cur_index = 0

        while cur_index <= border_r:
            if arr[cur_index] == 0:
                arr[cur_index], arr[border_l] = arr[border_l], arr[cur_index]
                border_l += 1
            elif arr[cur_index] == 2:
                arr[cur_index], arr[border_r] = arr[border_r], arr[cur_index]
                border_r -= 1
                cur_index -= 1
            cur_index += 1


arr_1 = [2, 0, 2, 1, 1, 0]
Solution.sort_colors_best(arr_1)
assert arr_1 == [0, 0, 1, 1, 2, 2]

arr_1 = [2, 0, 1]
Solution.sort_colors_best(arr_1)
assert arr_1 == [0, 1, 2]

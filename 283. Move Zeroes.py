"""Given an integer array nums, move all 0's to the end of it while
maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:
Input: nums = [0]
Output: [0]

Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
Follow up: Could you minimize the total number of operations done?"""
from typing import List


class Solution:
    @staticmethod
    def move_zeroes(nums: List[int]) -> None:
        """Do not return anything, modify nums in-place instead."""
        len_sequence = len(nums)
        first_cursor = 0
        second_cursor = 1

        while second_cursor < len_sequence:
            if nums[first_cursor] and nums[second_cursor]:
                first_cursor += 2
                second_cursor += 2
            elif nums[first_cursor] and not nums[second_cursor]:
                first_cursor += 1
                second_cursor += 1
            elif not nums[first_cursor] and nums[second_cursor]:
                nums[first_cursor], nums[second_cursor] = (nums[second_cursor],
                                                           nums[first_cursor])
            else:
                second_cursor += 1


if __name__ == '__main__':
    sequence = [0, 1, 0, 3, 12]
    Solution.move_zeroes(sequence)
    print(sequence)
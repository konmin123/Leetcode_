"""You have a set of integers s, which originally contains all the numbers from
1 to n. Unfortunately, due to some error, one of the numbers in s got
duplicated to another number in the set, which results in repetition of one
number and loss of another number.
You are given an integer array nums representing the data status of this set
after the error.
Find the number that occurs twice and the number that is missing and return
them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]

Example 2:
Input: nums = [1,1]
Output: [1,2]

Constraints:
2 <= nums.length <= 104
1 <= nums[i] <= 104"""
from typing import List


class Solution:
    @staticmethod
    def find_error_nums(nums: List[int]) -> List[int]:
        if nums[0] == 2:
            return [2, 1]
        prev_value = 0
        output_list = [0, 0]
        for value in nums:
            if value - 1 != prev_value:
                output_list[1] = value + 1
                output_list[0] = prev_value
                break
            prev_value = value
        return output_list


assert Solution.find_error_nums([1, 2, 3, 4, 4]) == [4, 5]
assert Solution.find_error_nums([1, 2, 2, 4]) == [2, 3]
assert Solution.find_error_nums([1, 1]) == [1, 2]

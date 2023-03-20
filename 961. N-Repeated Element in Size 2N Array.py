"""You are given an integer array nums with the following properties:

nums.length == 2 * n.
nums contains n + 1 unique elements.
Exactly one element of nums is repeated n times.
Return the element that is repeated n times.

Example 1:
Input: nums = [1,2,3,3]
Output: 3

Example 2:
Input: nums = [2,1,2,5,3,2]
Output: 2

Example 3:
Input: nums = [5,1,5,2,5,3,5,4]
Output: 5

Constraints:

2 <= n <= 5000
nums.length == 2 * n
0 <= nums[i] <= 104
nums contains n + 1 unique elements and one of them is repeated exactly n
times."""
from typing import List


class Solution:
    @staticmethod
    def repeated_n_times_inplace(nums: List[int]) -> int:
        for index, value in enumerate(nums):
            if value in nums[index + 1:]:
                return value

    @staticmethod
    def repeated_n_times(nums: List[int]) -> int:
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                return num
            else:
                nums_dict[num] = 1


assert Solution.repeated_n_times_inplace([1, 2, 3, 3]) == 3
assert Solution.repeated_n_times_inplace([2, 1, 2, 5, 3, 2]) == 2
assert Solution.repeated_n_times_inplace([5, 1, 5, 2, 5, 3, 5, 4]) == 5

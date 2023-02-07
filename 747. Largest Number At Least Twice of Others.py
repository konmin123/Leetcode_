"""You are given an integer array nums where the largest integer is unique.
Determine whether the largest element in the array is at least twice as much as
every other number in the array. If it is, return the index of the largest
element, or return -1 otherwise.

Example 1:
Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.

Example 2:
Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.

Constraints:
2 <= nums.length <= 50
0 <= nums[i] <= 100
The largest element in nums is unique."""
from typing import List


class Solution:
    @staticmethod
    def dominant_index(nums: List[int]) -> int:
        max_value: int = max(nums)
        index_max_value: int = nums.index(max_value)
        nums[index_max_value] = -1
        prev_max_value: int = max(nums)
        return index_max_value if max_value / prev_max_value >= 2 else - 1


assert Solution.dominant_index([3, 6, 1, 0]) == 1
assert Solution.dominant_index([1, 2, 3, 4]) == - 1

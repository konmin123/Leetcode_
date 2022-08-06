"""219. Contains Duplicate II
Easy

Given an integer array nums and an integer k, return true if there are two distinct indices i and j
in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Constraints:

    1 <= nums.length <= 105
    -109 <= nums[i] <= 109
    0 <= k <= 105
"""
from typing import List


class Solution:
    @staticmethod
    def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
        dict_values = {}
        for i in range(len(nums)):
            if nums[i] in dict_values:
                if i - dict_values.get(nums[i]) <= k:
                    return True
            dict_values[nums[i]] = i
        return False


if __name__ == '__main__':
    print(Solution.contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2))

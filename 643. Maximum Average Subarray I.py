"""You are given an integer array nums consisting of n elements, and an
integer k.
Find a contiguous subarray whose length is equal to k that has the maximum
average value and return this value. Any answer with a calculation error less
than 10-5 will be accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000

Constraints:
n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104"""
from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def find_max_average(nums: List[int], k: int) -> float:
        dict_average_sum = defaultdict(float)
        for variant in range(len(nums) - k + 1):
            average = sum(nums[variant:variant + k]) / k
            dict_average_sum[variant] = average
        return max(dict_average_sum.values())


assert Solution.find_max_average([1, 12, -5, -6, 50, 3], 4) == 12.75000
assert Solution.find_max_average([5], 1) == 5.00000
assert Solution.find_max_average([1, 15, 2, 14, 3, 13], 2) == 8.50000

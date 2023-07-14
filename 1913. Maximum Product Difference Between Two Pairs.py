"""
The product difference between two pairs (a, b) and (c, d) is defined as
(a * b) - (c * d). For example, the product difference between (5, 6) and
(2, 7) is (5 * 6) - (2 * 7) = 16. Given an integer array nums, choose four
distinct indices w, x, y, and z such that the product difference between pairs
(nums[w], nums[x]) and (nums[y], nums[z]) is maximized. Return the maximum such
product difference.

Example 1:
Input: nums = [5,6,2,7,4]
Output: 34
Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and
indices 2 and 4 for the second pair (2, 4). The product difference is
(6 * 7) - (2 * 4) = 34.

Example 2:
Input: nums = [4,2,5,9,7,4,8]
Output: 64
Explanation: We can choose indices 3 and 6 for the first pair (9, 8) and
indices 1 and 5 for the second pair (2, 4). The product difference is
(9 * 8) - (2 * 4) = 64.

Constraints:
4 <= nums.length <= 104
1 <= nums[i] <= 104
"""
from typing import List
from collections import defaultdict


class Solution:
    @staticmethod
    def max_product_difference_sort(nums: List[int]) -> int:
        nums.sort()
        return (nums[-2] * nums[-1]) - (nums[0] * nums[1])

    @staticmethod
    def max_product_difference(nums: List[int]) -> int:
        dict_count = defaultdict(int)

        for number in nums:
            dict_count[number] += 1

        max_number = max(dict_count)
        min_number = min(dict_count)

        for number in max_number, min_number:
            if dict_count[number] == 1:
                dict_count.pop(number)

        pre_max_number = max(dict_count)
        pre_min_number = min(dict_count)

        return (max_number * pre_max_number) - (min_number * pre_min_number)


assert Solution.max_product_difference([5, 6, 2, 7, 4]) == 34
assert Solution.max_product_difference([4, 2, 5, 9, 7, 4, 8]) == 64
assert Solution.max_product_difference_sort([5, 6, 2, 7, 4]) == 34
assert Solution.max_product_difference_sort([4, 2, 5, 9, 7, 4, 8]) == 64

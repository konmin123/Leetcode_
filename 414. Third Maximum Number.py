"""Given an integer array nums, return the third distinct maximum number in
this array. If the third maximum does not exist, return the maximum number.

Example 1:
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.

Example 2:
Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned
instead.

Example 3:
Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have
the same value).
The third distinct maximum is 1.

Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

Follow up: Can you find an O(n) solution?"""

from typing import List


class Solution:
    @staticmethod
    def brutal_force_third_max(nums: List[int]) -> int:
        first_max = -232
        second_max = -232
        third_max = -232
        for value in nums:
            if value > first_max:
                third_max = second_max
                second_max = first_max
                first_max = value
            elif value > second_max:
                third_max = second_max
                second_max = value
            elif value > third_max:
                third_max = value
        if (third_max != -232) and (third_max != second_max):
            return third_max
        return first_max

    @staticmethod
    def set_third_max(nums: List[int]) -> int:
        uniq_nums = set(nums)
        if len(uniq_nums) < 3:
            return max(uniq_nums)
        uniq_nums.remove(max(uniq_nums))
        uniq_nums.remove(max(uniq_nums))
        return max(uniq_nums)


print(Solution.set_third_max([2, 2, 3]))

"""You are given a binary array nums (0-indexed). We define xi as the number
whose binary representation is the subarray nums[0..i] (from
most-significant-bit to least-significant-bit). For example, if nums = [1,0,1],
then x0 = 1, x1 = 2, and x2 = 5. Return an array of booleans answer where
answer[i] is true if xi is divisible by 5.

Example 1:
Input: nums = [0,1,1]
Output: [true,false,false]
Explanation: The input numbers in binary are 0, 01, 011; which are 0, 1, and 3
in base-10. Only the first number is divisible by 5, so answer[0] is true.

Example 2:
Input: nums = [1,1,1]
Output: [false,false,false]

Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1."""
from typing import List


class Solution:
    @staticmethod
    def prefixes_div_by_5(nums: List) -> List:
        str_for_check = ''
        for index, element in enumerate(nums):
            str_for_check += str(element)
            if int(str_for_check, 2) % 5 == 0:
                nums[index] = True
            else:
                nums[index] = False
        return nums


assert Solution.prefixes_div_by_5([0, 1, 1]) == [True, False, False]
assert Solution.prefixes_div_by_5([1, 1, 1]) == [False, False, False]
assert Solution.prefixes_div_by_5([1, 1, 1, 1]) == [False, False, False, True]

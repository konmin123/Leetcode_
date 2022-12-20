"""Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear
in nums.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:
Input: nums = [1,1]
Output: [2]

Constraints:
n == nums.length
1 <= n <= 105
1 <= nums[i] <= n

Follow up: Could you do it without extra space and in O(n) runtime?
You may assume the returned list does not count as extra space."""
from typing import List


class Solution:
    @staticmethod
    def find_disappeared_numbers(nums: List[int]) -> List[int]:
        output = [1]
        while output[-1] != max(nums) + 1:
            if output[-1] in nums:
                output[-1] += 1
            else:
                output.append(output[-1] + 1)
        if len(output) > 1:
            output.pop()
        return output

    @staticmethod
    def find_disappeared_numbers2(nums: List[int]) -> List[int]:
        output = [x for x in range(1, max(nums)) if x not in nums]
        if not output:
            output.append(max(nums) + 1)
        return output


print(Solution.find_disappeared_numbers2([4]))

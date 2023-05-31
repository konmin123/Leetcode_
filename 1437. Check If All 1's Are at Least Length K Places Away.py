"""Given an binary array nums and an integer k, return true if all 1's are at
least k places away from each other, otherwise return false.

Example 1:
Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.

Example 2:
Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other.

Constraints:
1 <= nums.length <= 105
0 <= k <= nums.length
nums[i] is 0 or 1"""
from typing import List


class Solution:
    @staticmethod
    def k_length_apart(nums: List[int], k: int) -> bool:
        count: int = k
        for value in nums:
            if value:
                if count < k:
                    return False
                count = 0
            else:
                count += 1
        return True


assert Solution.k_length_apart([1, 0, 0, 0, 1, 0, 0, 1], 2)
assert not Solution.k_length_apart([1, 0, 0, 1, 0, 1], 2)

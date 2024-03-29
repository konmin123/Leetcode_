"""Given the array nums, for each nums[i] find out how many numbers in the
array are smaller than it. That is, for each nums[i] you have to count the
number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

Example 1:
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation:
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1).
For nums[3]=2 there exist one smaller number than it (1).
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

Example 2:
Input: nums = [6,5,4,8]
Output: [2,1,0,3]

Example 3:
Input: nums = [7,7,7,7]
Output: [0,0,0,0]

Constraints:
2 <= nums.length <= 500
0 <= nums[i] <= 100"""
from typing import List


class Solution:
    @staticmethod
    def smaller_numbers_than_current_brutal(nums: List[int]) -> List[int]:
        output = []
        for index, value in enumerate(nums):
            count = 0
            for i, val in enumerate(nums):
                if index != i and value > val:
                    count += 1
            output.append(count)
        return output

    @staticmethod
    def smaller_numbers_than_current(nums: List[int]) -> List[int]:
        count = [0] * 102
        output = []
        for num in nums:
            count[num + 1] = count[num + 1] + 1
        for i in range(1, 102):
            count[i] = count[i] + count[i - 1]
        for num in nums:
            output.append(count[num])
        return output


assert Solution.smaller_numbers_than_current(
    [8, 1, 2, 2, 3]) == [4, 0, 1, 1, 3]
assert Solution.smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3]
assert Solution.smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0]

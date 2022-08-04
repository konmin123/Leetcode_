"""Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:

    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109

Follow-up: Could you solve the problem in linear time and in O(1) space?"""
from typing import List


class Solution:
    @staticmethod
    def majority_element(nums: List[int]) -> int:
        dict_elem = {}
        for elem in nums:
            if elem in dict_elem:
                dict_elem[elem] += 1
            else:
                dict_elem[elem] = 1
        if max(dict_elem.values()) > len(nums)/2:
            return max(dict_elem, key=dict_elem.get)


if __name__ == '__main__':
    print(Solution.majority_element([2,2,1,1,1,2,2]))
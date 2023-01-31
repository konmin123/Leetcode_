"""Given a non-empty array of non-negative integers nums, the degree of this
array is defined as the maximum frequency of any one of its elements.
Your task is to find the smallest possible length of a (contiguous) subarray of
nums, that has the same degree as nums.

Example 1:
Input: nums = [1,2,2,3,1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:
Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation:
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.

Constraints:
nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999."""
from typing import List
from collections import defaultdict


class Solution:
    @staticmethod
    def find_shortest_sub_array(nums: List[int]) -> int:
        count_elem = defaultdict(int)
        for index, value in enumerate(nums):
            count_elem[str(value)] += 1
        max_count_elem_list = [
            x[0] for x in count_elem.items()
            if x[1] == max(count_elem.values())
        ]
        answer_list = []
        for elem in max_count_elem_list:
            left = nums.index(int(elem))
            right = (nums[::-1]).index(int(elem))
            answer_list.append(len(nums) - left - right)
        return min(answer_list)


assert Solution.find_shortest_sub_array([1, 2, 2, 3, 1]) == 2
assert Solution.find_shortest_sub_array([1, 2, 2, 3, 1, 4, 2]) == 6

"""Given two sorted arrays nums1 and nums2 of size m and n respectively, return
the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106
"""
from typing import List


class Solution:
    @staticmethod
    def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
        merge_array: List = nums1 + nums2
        merge_array.sort()
        len_array = len(merge_array)
        if len(merge_array) % 2 == 0:
            return ((merge_array[len_array//2 - 1] +
                    merge_array[len_array//2]) / 2)
        else:
            return merge_array[len_array//2]


assert Solution.find_median_sorted_arrays([1, 3], [2]) == 2
assert Solution.find_median_sorted_arrays([1, 2], [3, 4]) == 2.5

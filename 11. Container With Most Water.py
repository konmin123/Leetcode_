"""
You are given an integer array height of length n. There are n vertical lines
drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i])
Find two lines that together with the x-axis form a container, such that the
container contains the most water. Return the maximum amount of water a
container can store. Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array
[1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""
from typing import List


class Solution:
    @staticmethod
    def max_area_brutal(height: List[int]) -> int:
        max_area = 1
        for index_left, left in enumerate(height):
            for index_right, right in enumerate(height[index_left + 1:]):
                min_border = min(left, right)
                len_ = index_right + 1
                if min_border * len_ > max_area:
                    max_area = min_border * len_
        return max_area


assert Solution.max_area_brutal([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert Solution.max_area_brutal([1, 1]) == 1

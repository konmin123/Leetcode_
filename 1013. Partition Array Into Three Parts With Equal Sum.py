"""Given an array of integers arr, return true if we can partition the array
into three non-empty parts with equal sums. Formally, we can partition the
array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] ==
arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ...
+ arr[arr.length - 1])

Example 1:
Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

Example 2:
Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false

Example 3:
Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

Constraints:
3 <= arr.length <= 5 * 104
-104 <= arr[i] <= 104"""
from typing import List


class Solution:
    @staticmethod
    def can_three_parts_equal_sum(arr: List[int]) -> bool:
        if sum(arr) % 3 != 0:
            return False
        value = sum(arr) // 3
        left_cur = 1
        right_cur = -1
        while sum(arr[:left_cur]) < value:
            left_cur += 1
        while sum(arr[right_cur:]) < value:
            right_cur -= 1
        return sum(arr[:left_cur]) == sum(arr[right_cur:]) == value


assert Solution.can_three_parts_equal_sum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1])
assert not Solution.can_three_parts_equal_sum(
    [0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]
)
assert Solution.can_three_parts_equal_sum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4])


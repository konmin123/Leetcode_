"""Given a fixed-length integer array arr, duplicate each occurrence of zero,
shifting the remaining elements to the right. Note that elements beyond the
length of the original array are not written. Do the above modifications to
the input array in place and do not return anything.

Example 1:
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to:
[1,0,0,2,3,0,0,4]

Example 2:
Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to:
[1,2,3]

Constraints:
1 <= arr.length <= 104
0 <= arr[i] <= 9"""
from typing import List
from collections import deque


class Solution:
    @staticmethod
    def duplicate_zeros(arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        queue_elements = deque()
        for index, value in enumerate(arr):
            if queue_elements:
                queue_elements.append(value)
                arr[index] = queue_elements.popleft()
            if value == 0:
                queue_elements.append(value)
        print(arr)


Solution.duplicate_zeros([0, 0, 0, 1, 2, 3])

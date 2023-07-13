"""
Given an array of integers arr, a lucky integer is an integer that has a
frequency in the array equal to its value. Return the largest lucky integer
in the array. If there is no lucky integer return -1.

Example 1:
Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.

Example 2:
Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

Example 3:
Input: arr = [2,2,2,3,3]
Output: -1
Explanation: There are no lucky numbers in the array.

Constraints:
1 <= arr.length <= 500
1 <= arr[i] <= 500
"""
from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def find_lucky(arr: List[int]) -> int:
        dict_count = defaultdict(int)  # O(1)
        for number in arr:  # O(n)
            dict_count[number] += 1
        dict_count = {x[0] for x in dict_count.items() if x[0] == x[1]}  # O(n)
        return max(dict_count) if dict_count else -1  # O(len(dict(count)))


assert Solution.find_lucky([2, 2, 3, 4]) == 2
assert Solution.find_lucky([1, 2, 2, 3, 3, 3]) == 3
assert Solution.find_lucky([2, 2, 2, 3, 3]) == -1

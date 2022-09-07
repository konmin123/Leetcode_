from typing import List

"""You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is,
each element of nums is covered by exactly one of the ranges,
and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

    "a->b" if a != b
    "a" if a == b

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

Constraints:

    0 <= nums.length <= 20
    -231 <= nums[i] <= 231 - 1
    All the values of nums are unique.
    nums is sorted in ascending order.

"""


class Solution:
    def __init__(self):
        self.start = None
        self.stop = None
        self.next_value = None

    def summary_ranges(self, nums: List[int]) -> List[str]:
        nums.append(1)
        self.start = nums[0]
        self.stop = nums[0]
        self.next_value = nums[0]
        output = []
        for value in nums:
            if self.next_value != value:
                if self.start == self.stop:
                    output.append(str(self.start))
                else:
                    output.append(str(self.start) + '->' + str(self.stop))
                self.start = value
                self.stop = value
                self.next_value = value + 1
            else:
                self.next_value += 1
                self.stop = value
        return output


if __name__ == '__main__':
    s = Solution()
    print(s.summary_ranges([0, 1, 2, 4, 5, 7]))

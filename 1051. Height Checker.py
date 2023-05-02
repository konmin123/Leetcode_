"""A school is trying to take an annual photo of all the students. The students
are asked to stand in a single file line in non-decreasing order by height.
Let this ordering be represented by the integer array expected where
expected[i] is the expected height of the ith student in line. You are given
an integer array heights representing the current order that the students are
standing in. Each heights[i] is the height of the ith student in line
(0-indexed). Return the number of indices where heights[i] != expected[i].

Example 1:
Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation:
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Indices 2, 4, and 5 do not match.

Example 2:
Input: heights = [5,1,2,3,4]
Output: 5
Explanation:
heights:  [5,1,2,3,4]
expected: [1,2,3,4,5]
All indices do not match.

Example 3:
Input: heights = [1,2,3,4,5]
Output: 0
Explanation:
heights:  [1,2,3,4,5]
expected: [1,2,3,4,5]
All indices match.

Constraints:
1 <= heights.length <= 100
1 <= heights[i] <= 100"""
from typing import List


class Solution:
    def __init__(self, seq: List[int]):
        self.seq = seq

    def height_checker(self) -> int:
        sort_seq: List[int] = sorted(self.seq)
        output: int = 0
        for index in range(len(sort_seq)):
            if sort_seq[index] != self.seq[index]:
                output += 1
        return output

    def height_checker_zip(self) -> int:
        return sum(a != b for a, b in zip(self.seq, sorted(self.seq)))


test_1 = Solution([1, 1, 4, 2, 1, 3])
assert test_1.height_checker() == 3
assert test_1.height_checker_zip() == 3

test_2 = Solution([5, 1, 2, 3, 4])
assert test_2.height_checker() == 5
assert test_2.height_checker_zip() == 5

test_3 = Solution([1, 2, 3, 4, 5])
assert test_3.height_checker() == 0
assert test_3.height_checker_zip() == 0

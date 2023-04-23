"""Given a m x n matrix grid which is sorted in non-increasing order both
row-wise and column-wise, return the number of negative numbers in grid.

Example 1:
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example 2:
Input: grid = [[3,2],[1,0]]
Output: 0

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100
Follow up: Could you find an O(n + m) solution?"""
from typing import List


class Solution:
    @staticmethod
    def count_negatives(grid: List[List[int]]) -> int:
        count_: int = 0
        start_pos: int = 0
        for seq in grid[::-1]:
            for index, element in enumerate(seq[start_pos:]):
                if element < 0:
                    count_ += len(seq) - index - start_pos
                    start_pos = index
                    break
        return count_


assert Solution.count_negatives(
    [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
) == 8
assert Solution.count_negatives([[3, 2], [1, 0]]) == 0

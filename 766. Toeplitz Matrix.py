"""Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise,
return false. A matrix is Toeplitz if every diagonal from top-left to
bottom-right has the same elements.

Example 1:
Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.

Example 2:
Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 20
0 <= matrix[i][j] <= 99


Follow up:
What if the matrix is stored on disk, and the memory is limited such that you
can only load at most one row of the matrix into the memory at once?
What if the matrix is so large that you can only load up a partial row into
the memory at once?"""
from typing import List


class Solution:
    @staticmethod
    def is_toeplitz_matrix(matrix: List[List[int]]) -> bool:
        len_line: int = len(matrix[0])
        len_matrix: int = len(matrix)
        for index, line in enumerate(matrix):
            if index + 1 < len_matrix:
                if line[:len_line - 1] != matrix[index + 1][1:]:
                    return False
        return True


assert Solution.is_toeplitz_matrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]])
assert Solution.is_toeplitz_matrix([[1, 2], [5, 1]])
assert not Solution.is_toeplitz_matrix([[1, 2], [2, 2]])

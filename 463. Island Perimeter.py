"""You are given row x col grid representing a map where grid[i][j] = 1
represents land and grid[i][j] = 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is
completely surrounded by water, and there is exactly one island (i.e., one or
more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to
the water around the island. One cell is a square with side length 1. The grid
is rectangular, width and height don't exceed 100. Determine the perimeter of
the island.

Example 1:
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

Example 2:
Input: grid = [[1]]
Output: 4

Example 3:
Input: grid = [[1,0]]
Output: 4

Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
There is exactly one island in grid."""
from typing import List


class Solution:
    @staticmethod
    def island_perimeter_brutal_force(grid: List[List[int]]) -> int:
        perimeter = 0
        for index_list, items_list in enumerate(grid):
            for index_item, item in enumerate(items_list):
                if item == 1:
                    add_sum = 4
                    if index_list != 0:
                        if grid[index_list - 1][index_item] == 1:
                            add_sum -= 1
                    if index_list + 1 < len(grid):
                        if grid[index_list + 1][index_item] == 1:
                            add_sum -= 1
                    if index_item != 0:
                        if items_list[index_item - 1] == 1:
                            add_sum -= 1
                    if index_item + 1 < len(items_list):
                        if items_list[index_item + 1] == 1:
                            add_sum -= 1
                    perimeter += add_sum
        return perimeter

    @staticmethod
    def island_perimeter(grid):
        area = 0
        for row in grid + list(map(list, zip(*grid))):
            for i1, i2 in zip([0] + row, row + [0]):
                area += int(i1 != i2)
        return area


print(Solution.island_perimeter(
    [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]])
)

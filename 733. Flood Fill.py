"""An image is represented by an m x n integer grid image where image[i][j]
represents the pixel value of the image. You are also given three integers sr,
sc, and color. You should perform a flood fill on the image starting from the
pixel image[sr][sc]. To perform a flood fill, consider the starting pixel, plus
any pixels connected 4-directionally to the starting pixel of the same color as
the starting pixel, plus any pixels connected 4-directionally to those pixels
(also with the same color), and so on. Replace the color of all of the
aforementioned pixels with color. Return the modified image after performing
the flood fill.

Example 1:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1)
(i.e., the red pixel), all pixels connected by a path of the same color as the
starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally
connected to the starting pixel.

Example 2:
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made
to the image.

Constraints:
m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], color < 216
0 <= sr < m
0 <= sc < n"""
from typing import List


class Solution:
    @staticmethod
    def flood_fill_rec(image: List, sr: int, sc: int, color: int) -> List:
        start_color = image[sr][sc]

        def flood_fill(x, y):

            if x < 0 or x >= len(image):
                return
            if y < 0 or y >= len(image[0]):
                return
            if image[x][y] == color:
                return
            if image[x][y] != start_color:
                return

            image[x][y] = color

            flood_fill(x - 1, y)
            flood_fill(x + 1, y)
            flood_fill(x, y - 1)
            flood_fill(x, y + 1)

        flood_fill(sr, sc)
        return image

    @staticmethod
    def flood_fill_it(image: List, sr: int, sc: int, color: int) -> List:
        m: list = [x for x in range(len(image))]
        n: list = [x for x in range(len(image[1]))]
        if not (sr in m and sc in n) or image[sr][sc] == color:
            return image
        neighbors: list = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        stack: list = [[sr, sc]]
        while stack:
            cur: list = stack.pop()
            cur_color: int = image[cur[0]][cur[1]]
            for nb in neighbors:
                if cur[0] + nb[0] in m and cur[1] + nb[1] in n:
                    if image[cur[0] + nb[0]][cur[1] + nb[1]] == cur_color:
                        if [cur[0] + nb[0], cur[1] + nb[1]] not in stack:
                            stack.append([cur[0] + nb[0], cur[1] + nb[1]])
            image[cur[0]][cur[1]] = color
        return image


assert Solution.flood_fill_rec([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) == [
    [2, 2, 2], [2, 2, 0], [2, 0, 1]
]
assert Solution.flood_fill_rec([[0, 0, 0], [0, 0, 0]], 0, 0, 0) == [
    [0, 0, 0], [0, 0, 0]
]
assert Solution.flood_fill_it([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) == [
    [2, 2, 2], [2, 2, 0], [2, 0, 1]
]
assert Solution.flood_fill_it([[0, 0, 0], [0, 0, 0]], 0, 0, 0) == [
    [0, 0, 0], [0, 0, 0]
]
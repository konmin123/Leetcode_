"""Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:



Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]
"""
from typing import List


class Solution:
    @staticmethod
    def generate(num_rows: int) -> List[List[int]]:
        output = []
        for i in range(1, num_rows + 1):
            if i == 1:
                output.append([1])
                continue
            if i == 2:
                output.append([1, 1])
                continue
            else:
                list_for_add = [1, 1]
                for j in range(1, len(output[-1])):
                    x = output[-1][j-1] + output[-1][j]
                    list_for_add.insert(j, x)
                output.append(list_for_add)
        return output


if __name__ == '__main__':
    print(Solution.generate(5))


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
            if i == 2:
                output.append([1, 1])
            else:
                list_for_add = []
                for j in range(len(output[-1])-1):
                    ...


        return output


if __name__ == '__main__':
    print(Solution.generate(5))


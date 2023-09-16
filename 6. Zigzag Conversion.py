"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
of rows like this: (you may want to display this pattern in a fixed font for
better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR". Write the code that will take a
string and make this conversion given a number of rows: string convert(
string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""
from itertools import cycle


class Solution:
    @staticmethod
    def convert(s: str, num_rows: int) -> str:
        num_rows_list = [[] for _ in range(num_rows)]
        order = ([x for x in range(num_rows)]
                 + [x for x in range(num_rows - 2, 0, -1)])
        index_generator = (x for x in cycle(order))
        for letter in s:
            index = next(index_generator)
            num_rows_list[index].append(letter)
        output = ''
        for list_letters in num_rows_list:
            output += ''.join(list_letters)
        return output


assert Solution.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
assert Solution.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"

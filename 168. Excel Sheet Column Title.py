"""Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...

Example 1:

Input: columnNumber = 1
Output: "A"

Example 2:

Input: columnNumber = 28
Output: "AB"

Example 3:

Input: columnNumber = 701
Output: "ZY"

Constraints:

    1 <= columnNumber <= 2**31 - 1
"""


class Solution:
    @staticmethod
    def convert_to_title(column_number: int) -> str:
        alphabet = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K", 12: "L",
                    13: "M", 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 21: "U", 22: "V", 23: "W",
                    24: "X", 25: "Y", 26: "Z"}
        column_number_for_while = column_number
        i = 1
        while column_number_for_while > 0:
            if column_number_for_while - 26 ** i > 0:
                column_number_for_while = column_number_for_while - 26 ** i
                i += 1
            else:
                break
        num = column_number
        output = ""
        for i_ in range(i-1, 0, -1):
            output += (alphabet[num // 26 ** i_])
            num = num - (26 ** i_) * (num // 26 ** i_)
        output += (alphabet[num])
        return str(output)


if __name__ == '__main__':
    print(Solution.convert_to_title(16381))
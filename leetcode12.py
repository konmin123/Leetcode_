"""Given two binary string a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"



Constraints:

    1 <= a.length, b.length <= 104
    a and b consist only of '0' or '1' characters.
    Each string does not contain leading zeros except for the zero itself."""

num1 = "1010"
num2 = "1011"


class Solution:
    @staticmethod
    def add_binary(a: str, b: str) -> str:
        int_ = int(a) + int(b)
        output = ''
        memory = 0
        for i in str(int_)[::-1]:
            if int(i) + memory == 0:
                output = '0' + output
                memory = 0
                continue
            if int(i) + memory == 1:
                output = '1' + output
                memory = 0
                continue
            if int(i) + memory == 2:
                output = '0' + output
                memory = 1
                continue
            if int(i) + memory == 3:
                output = '1' + output
                memory = 1
                continue
        if memory:
            output = '1' + output
        return output


if __name__ == '__main__':
    print(Solution.add_binary(num1, num2))
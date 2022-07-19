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

num1 = "11"
num2 = "0"


class Solution:
    @staticmethod
    def add_binary(a: str, b: str) -> str:
        int_ = int(a) + int(b)
        output = ''
        memory = 0
        dict_of_sum = {0: [0, 0], 1: [1, 0], 2: [0, 1], 3: [1, 1]}
        for i in str(int_)[::-1]:
            list_value = dict_of_sum[int(i) + memory]
            output = str(list_value[0]) + output
            memory = list_value[1]
            continue
        if memory:
            output = '1' + output
        return output


if __name__ == '__main__':
    print(Solution.add_binary(num1, num2))
    
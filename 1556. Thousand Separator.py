"""
Given an integer n, add a dot (".") as the thousands separator and return it
in string format.

Example 1:
Input: n = 987
Output: "987"

Example 2:
Input: n = 1234
Output: "1.234"

Constraints:
0 <= n <= 231 - 1
"""
import timeit


class Solution:
    @staticmethod
    def thousand_separator(n: int) -> str:
        output = []
        for index, letter in enumerate(str(n)[::-1]):
            if index and index % 3 == 0:
                output.append('.')
            output.append(letter)
        return ''.join(output[::-1])

    @staticmethod
    def thousand_separator_one_line(n: int) -> str:
        return f"{n:,}".replace(',', '.')


assert Solution.thousand_separator(987) == '987'
assert Solution.thousand_separator(1234) == '1.234'
assert Solution.thousand_separator_one_line(987) == '987'
assert Solution.thousand_separator_one_line(1234) == '1.234'


print(timeit.timeit(Solution.thousand_separator(1234), number=10000))
print(timeit.timeit(Solution.thousand_separator_one_line(1234), number=10000))

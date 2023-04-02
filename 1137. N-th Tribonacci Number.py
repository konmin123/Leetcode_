"""The Tribonacci sequence Tn is defined as follows:
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.

Example 1:
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:
Input: n = 25
Output: 1389537


Constraints:
0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie.
answer <= 2^31 - 1."""


class Solution:
    @staticmethod
    def tribonacci(n: int) -> int:
        start_list = [1, 1, 2]
        if n < 4:
            return start_list[n - 1]
        for _ in range(n - 3):
            start_list = [start_list[1], start_list[2], sum(start_list)]
        return start_list[-1]


assert Solution.tribonacci(1) == 1
assert Solution.tribonacci(2) == 1
assert Solution.tribonacci(3) == 2
assert Solution.tribonacci(4) == 4
assert Solution.tribonacci(25) == 1389537

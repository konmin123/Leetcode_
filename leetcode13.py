"""You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step"""

number_of_steps = 7


class Solution:
    @staticmethod
    def climb_stairs(n: int) -> int:
        if n <= 3:
            return n
        else:
            prev_prev = 2
            prev_ = 3
            current = prev_ + prev_prev
            for _ in range(n - 4):
                prev_, prev_prev = current, prev_
                current = prev_ + prev_prev
            return current


if __name__ == '__main__':
    print(Solution.climb_stairs(number_of_steps))
"""Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x."""
import math


class Solution:
    @staticmethod  # complexity log(N)
    def brutal_force(n: int) -> bool:
        if n == 1 or n == 2:
            return True
        number = 2
        while True:
            number *= 2
            if number == n:
                return True
            if number > n:
                return False

    @staticmethod
    def binary_solution(n: int) -> bool:
        binary = f'{n:0b}'
        binary_head = binary[:1]
        binary_tail = binary[1:]
        if binary_head == "1" and "1" not in binary_tail:
            return True
        return False

    @staticmethod
    def binary_search_solution(n: int) -> bool:
        left_border = 0
        right_border = math.log(n, 2)
        while left_border <= right_border:
            middle = int((left_border + right_border) / 2)
            if 2 ** middle == n:
                return True
            elif 2 ** middle < n:
                left_border = middle + 1
            else:
                right_border = middle + 1
        return False

    @staticmethod
    def math_log_solution(n: int) -> bool:
        float_ = math.log(n, 2)
        int_ = int(float_)
        if int_ == float_:
            return True
        return False


if __name__ == '__main__':
    print(Solution.math_log_solution(1028))


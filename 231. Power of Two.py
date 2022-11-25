"""Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x."""


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


if __name__ == '__main__':
    print(Solution.binary_solution(257))


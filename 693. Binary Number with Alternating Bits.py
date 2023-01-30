"""Given a positive integer, check whether it has alternating bits: namely, if
two adjacent bits will always have different values.

Example 1:
Input: n = 5
Output: true
Explanation: The binary representation of 5 is: 101

Example 2:
Input: n = 7
Output: false
Explanation: The binary representation of 7 is: 111.

Example 3:
Input: n = 11
Output: false
Explanation: The binary representation of 11 is: 1011.

Constraints:
1 <= n <= 231 - 1"""


class Solution:
    @staticmethod
    def has_alternating_bits_in(n: int) -> bool:
        binary_str = bin(n)
        return '00' not in binary_str and '11' not in binary_str

    @staticmethod
    def has_alternating_bits_count(n: int) -> bool:
        binary_str = bin(n)[2:]
        if len(binary_str) % 2 == 1:
            if binary_str[-1] == '1':
                binary_str = binary_str[:-1]
            else:
                return False
        return binary_str.count('10') == (len(binary_str) // 2)


assert Solution.has_alternating_bits_in(2)
assert Solution.has_alternating_bits_in(5)
assert Solution.has_alternating_bits_in(10)
assert not Solution.has_alternating_bits_in(7)
assert not Solution.has_alternating_bits_in(11)

"""Given an integer number n, return the difference between the product of its
digits and the sum of its digits.

Example 1:
Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15

Example 2:
Input: n = 4421
Output: 21
Explanation:
Product of digits = 4 * 4 * 2 * 1 = 32
Sum of digits = 4 + 4 + 2 + 1 = 11
Result = 32 - 11 = 21"""


class Solution:
    @staticmethod
    def subtract_product_and_sum(n: int) -> int:
        product_of_digits: int = 1
        sum_of_digits: int = 0
        for number in str(n):
            product_of_digits *= int(number)
            sum_of_digits += int(number)
        return product_of_digits - sum_of_digits


assert Solution.subtract_product_and_sum(234) == 15
assert Solution.subtract_product_and_sum(4421) == 21

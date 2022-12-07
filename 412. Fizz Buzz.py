"""Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

Example 1:
Input: n = 3
Output: ["1","2","Fizz"]

Example 2:
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

Example 3:
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz",
"13","14","FizzBuzz"]

Constraints:
1 <= n <= 104"""
from typing import List


class Solution:
    @staticmethod
    def fizz_buzz(n: int) -> List[str]:
        answer_list = []
        for number in range(1, n+1):
            if number % 3 == 0 and number % 5 == 0:
                answer_list.append('FizzBuzz')
            elif number % 3 == 0:
                answer_list.append('Fizz')
            elif number % 5 == 0:
                answer_list.append('Buzz')
            else:
                answer_list.append(str(number))
        return answer_list


if __name__ == '__main__':
    print(Solution.fizz_buzz(5))
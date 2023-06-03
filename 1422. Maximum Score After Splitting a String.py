"""Given a string s of zeros and ones, return the maximum score after splitting
the string into two non-empty substrings (i.e. left substring and right
substring). The score after splitting a string is the number of zeros in the
left substring plus the number of ones in the right substring.

Example 1:
Input: s = "011101"
Output: 5
Explanation:
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5
left = "01" and right = "1101", score = 1 + 3 = 4
left = "011" and right = "101", score = 1 + 2 = 3
left = "0111" and right = "01", score = 1 + 1 = 2
left = "01110" and right = "1", score = 2 + 1 = 3

Example 2:
Input: s = "00111"
Output: 5
Explanation: When left = "00" and right = "111", we get the maximum score =
2 + 3 = 5

Example 3:
Input: s = "1111"
Output: 3

Constraints:
2 <= s.length <= 500
The string s consists of characters '0' and '1' only."""


class Solution:
    @staticmethod
    def max_score_brutal(str_) -> int:
        max_sum: int = 0
        for index in range(1, len(str_)):
            left: int = str_[:index].count('0')
            right: int = str_[index:].count('1')
            if left + right > max_sum:
                max_sum = left + right
        return max_sum

    @staticmethod
    def max_score(str_: str) -> int:
        max_sum = 0
        zeros = 0
        ones = str_.count("1")
        for i in range(len(str_)):
            if str_[i] == "0":
                zeros += 1
            else:
                ones -= 1
            if i == len(str_) - 1:
                continue
            if zeros + ones > max_sum:
                max_sum = zeros + ones
        return max_sum


assert Solution.max_score_brutal("011101") == 5
assert Solution.max_score_brutal("00111") == 5
assert Solution.max_score_brutal("1111") == 3

assert Solution.max_score("011101") == 5
assert Solution.max_score("00111") == 5
assert Solution.max_score("1111") == 3

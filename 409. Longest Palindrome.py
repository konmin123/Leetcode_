"""Given a string s which consists of lowercase or uppercase letters, return
the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome
here.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd",
 whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length
is 1.

Constraints:
1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only."""
from collections import defaultdict


class Solution:
    @staticmethod
    def longest_palindrome(s: str) -> int:
        lower_case_string = str.lower(s)
        letters_dict = defaultdict(int)
        for letter in lower_case_string:
            letters_dict[letter] += 1
        simple_letter_flag = False
        answer_number = 0
        for item in letters_dict.items():
            if item[1] % 2 == 1:
                simple_letter_flag = True
            if item[1] >= 2:
                answer_number += item[1] - item[1] % 2
        return answer_number + simple_letter_flag


if __name__ == '__main__':
    print(Solution.longest_palindrome('aabbbc'))




"""We define the usage of capitals in a word to be right when one of the
following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

Example 1:
Input: word = "USA"
Output: true

Example 2:
Input: word = "FlaG"
Output: false

Constraints:
1 <= word.length <= 100
word consists of lowercase and uppercase English letters."""


class Solution:
    @staticmethod
    def detect_capital_use(word: str) -> bool:
        set_variants = [word.capitalize(), word.lower(), word.upper()]
        if word in set_variants:
            return True
        return False


print(Solution.detect_capital_use('WWWeR'))

"""Given an array of string words, return all strings in words that is a
substring of another word. You can return the answer in any order.
A substring is a contiguous sequence of characters within a string

Example 1:
Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of
"superhero". ["hero","as"] is also a valid answer.

Example 2:
Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".

Example 3:
Input: words = ["blue","green","bu"]
Output: []
Explanation: No string of words is substring of another string.

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 30
words[i] contains only lowercase English letters.
All the strings of words are unique."""
from typing import List


class Solution:
    @staticmethod
    def string_matching(words: List[str]) -> List[str]:
        words.sort(key=len)
        output: list = []
        for index, substring in enumerate(words):
            for word in words[index + 1:]:
                if substring in word:
                    output.append(substring)
                    break
        return output


assert Solution.string_matching(
    ['mass', 'as', 'hero', 'superhero']) == ['as', 'hero']

assert Solution.string_matching(
    ['leetcode', 'et', 'code']) == ['et', 'code']

assert Solution.string_matching(
    ['blue', 'green', 'bu']) == []

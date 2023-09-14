"""
You are given a 0-indexed string word, consisting of lowercase English letters.
You need to select one index and remove the letter at that index from word so
that the frequency of every letter present in word is equal. Return true if it
is possible to remove one letter so that the frequency of all letters in word
are equal, and false otherwise.

Note:
The frequency of a letter x is the number of times it occurs in the string.
You must remove exactly one letter and cannot chose to do nothing.

Example 1:
Input: word = "abcc"
Output: true
Explanation: Select index 3 and delete it: word becomes "abc" and each
character has a frequency of 1.

Example 2:
Input: word = "aazz"
Output: false
Explanation: We must delete a character, so either the frequency of "a" is 1
and the frequency of "z" is 2, or vice versa. It is impossible to make all
present letters have equal frequency.

Constraints:
2 <= word.length <= 100
word consists of lowercase English letters only.
"""
from collections import defaultdict


class Solution:
    @staticmethod
    def equal_frequency(word: str) -> bool:
        count_letters = defaultdict(int)
        for letter in word:
            count_letters[letter] += 1
        count_list = []
        for item in count_letters.items():
            if item[1] not in count_list:
                count_list.append(item[1])
        return len(count_list) == 2 and max(count_list) - min(count_list) == 1


assert Solution.equal_frequency("abcc")
assert not Solution.equal_frequency("aazz")
assert Solution.equal_frequency("aabbccddd")

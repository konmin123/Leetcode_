"""Given a string array words, return an array of all characters that show up
in all strings within the words (including duplicates). You may return the
answer in any order.

Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters."""
from typing import List


class Solution:
    @staticmethod
    def common_chars(words: List[str]) -> List[str]:
        letters = set(words[0])
        output = []
        for letter in letters:
            count_ = []
            for word in words:
                count_.append(word.count(letter))
            for _ in range(min(count_)):
                output.append(letter)
        return sorted(output)


assert Solution.common_chars(["bella", "label", "roller"]) == ["e", "l", "l"]
assert Solution.common_chars(["cool", "lock", "cook"]) == ["c", "o"]

"""Given a 0-indexed string word and a character ch, reverse the segment of
word that starts at index 0 and ends at the index of the first occurrence of ch
(inclusive). If the character ch does not exist in word, do nothing.

For example, if word = "abcdefd" and ch = "d", then you should reverse the
segment that starts at 0 and ends at 3 (inclusive). The resulting string will
be "dcbaefd".

Return the resulting string.

Example 1:
Input: word = "abcdefd", ch = "d"
Output: "dcbaefd"
Explanation: The first occurrence of "d" is at index 3.
Reverse the part of word from 0 to 3 (inclusive), the resulting string is
"dcbaefd".

Example 2:
Input: word = "xyxzxe", ch = "z"
Output: "zxyxxe"
Explanation: The first and only occurrence of "z" is at index 3.
Reverse the part of word from 0 to 3 (inclusive), the resulting string is
"zxyxxe".

Example 3:
Input: word = "abcd", ch = "z"
Output: "abcd"
Explanation: "z" does not exist in word.
You should not do any reverse operation, the resulting string is "abcd".

Constraints:
1 <= word.length <= 250
word consists of lowercase English letters.
ch is a lowercase English letter."""


class Solution:
    @staticmethod
    def reverse_prefix(word: str, ch: str) -> str:
        if ch in word:
            ch_index = word.index(ch)
            return word[:ch_index + 1][::-1] + word[ch_index + 1:]
        return word


assert Solution.reverse_prefix("abcdefd", "d") == "dcbaefd"
assert Solution.reverse_prefix("xyxzxe", "z") == "zxyxxe"
assert Solution.reverse_prefix("abcd", "z") == "abcd"

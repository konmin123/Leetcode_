"""Given a string s, reverse the order of characters in each word within a
sentence while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
Input: s = "God Ding"
Output: "doG gniD"

Constraints:
1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space."""


class Solution:
    @staticmethod
    def reverse_words_str(s: str) -> str:
        output: str = ''
        for word in s.split():
            output += word[::-1] + ' '
        return output.strip(' ')

    @staticmethod
    def reverse_words_list(s: str) -> str:
        output_list: list = s.split()
        for index, word in enumerate(output_list):
            output_list[index] = word[::-1]
        return ' '.join(output_list)


assert Solution.reverse_words_str(
    "Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
assert Solution.reverse_words_str("God Ding") == "doG gniD"
assert Solution.reverse_words_list(
    "Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
assert Solution.reverse_words_list("God Ding") == "doG gniD"
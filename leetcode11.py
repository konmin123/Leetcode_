"""Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.



Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.



Constraints:

    1 <= s.length <= 104
    s consists of only English letters and spaces ' '.
    There will be at least one word in s.

"""

str_ = "Hello World"


class Solution:
    @staticmethod
    def length_of_last_word(s: str) -> int:
        s_for_use = "  " + s
        met_word = False
        index_symbol = -1
        len_word = 0
        while True:
            if s_for_use[index_symbol].isalpha():
                met_word = True
                len_word += 1
            elif met_word:
                break
            index_symbol -= 1
        return len_word


if __name__ == '__main__':
    print(Solution.length_of_last_word(str_))




"""Given an array of strings words, return the words that can be typed using
letters of the alphabet on only one row of American keyboard like the image
below.

In the American keyboard:
the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

Example 1:
Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]

Example 2:
Input: words = ["omk"]
Output: []

Example 3:
Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]

Constraints:
1 <= words.length <= 20
1 <= words[i].length <= 100
words[i] consists of English letters (both lowercase and uppercase). """
from typing import List


class Solution:
    @staticmethod
    def find_words(words: List[str]) -> List[str]:
        letters_dict = {
            'q': 1, 'w': 1, 'e': 1, 'r': 1, 't': 1, 'y': 1, 'u': 1, 'i': 1,
            'o': 1, 'p': 1, 'a': 2, 's': 2, 'd': 2, 'f': 2, 'g': 2, 'h': 2,
            'j': 2, 'k': 2, 'l': 2, 'z': 3, 'x': 3, 'c': 3, 'v': 3, 'b': 3,
            'n': 3, 'm': 3
        }
        output = []
        for word in words:
            word_in_one_row = True
            first_letter_row = letters_dict[word[0].lower()]
            for letter in word[1:]:
                if letters_dict[letter.lower()] != first_letter_row:
                    word_in_one_row = False
                    break
            if word_in_one_row:
                output.append(word)
        return output


assert Solution.find_words(
    ["Hello", "Alaska", "Dad", "Peace"]) == ["Alaska", "Dad"]
assert Solution.find_words(
    ["omk"]) == []
assert Solution.find_words(
    ["adsdf", "sfd"]) == ["adsdf", "sfd"]

"""You are given a string s. Reorder the string using the following algorithm:
Pick the smallest character from s and append it to the result.
Pick the smallest character from s which is greater than the last appended
character to the result and append it. Repeat step 2 until you cannot pick more
characters. Pick the largest character from s and append it to the result.
Pick the largest character from s which is smaller than the last appended
character to the result and append it. Repeat step 5 until you cannot pick
more characters. Repeat the steps from 1 to 6 until you pick all characters
from s. In each step, If the smallest or the largest character appears more
than once you can choose any occurrence and append it to the result.
Return the result string after sorting s with this algorithm.

Example 1:
Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"

Example 2:
Input: s = "rat"
Output: "art"
Explanation: The word "rat" becomes "art" after re-ordering it with the
mentioned algorithm."""
from collections import defaultdict
from itertools import cycle


class Solution:
    @staticmethod
    def sort_string(s: str) -> str:
        letters_count: dict = defaultdict(int)
        for letter in s:
            letters_count[letter] += 1
        letters: list = sorted(list(letters_count))
        letters = letters + letters[::-1]
        iterator_cycle = iter(cycle(letters))
        output_list: list = []
        for _ in s:
            current_letter = next(iterator_cycle)
            if letters_count[current_letter] > 0:
                letters_count[current_letter] -= 1
                output_list.append(current_letter)
            else:
                break
        return ''.join(output_list)


assert Solution.sort_string("aaaabbbbcccc") == "abccbaabccba"
assert Solution.sort_string("rat") == "art"

"""Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false
Constraints:
    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""


class Solution:
    @staticmethod
    def is_anagram(s: str, t: str) -> bool:
        first_str = sorted(s)
        second_str = sorted(t)
        if first_str == second_str:
            return True
        else:
            return False


if __name__ == '__main__':
    print(Solution.is_anagram('kos/tja', 'oksatj/'))
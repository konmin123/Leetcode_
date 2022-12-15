"""Given two strings ransomNote and magazine, return true if ransomNote can be
constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters."""


class Solution:
    @staticmethod
    def can_construct(ransom_note: str, magazine: str) -> bool:
        for letter in ransom_note:
            if ransom_note.count(letter) > magazine.count(letter):
                return False
        return True


print(Solution.can_construct('aa', 'aabb'))
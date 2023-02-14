"""Given two strings s and goal, return true if you can swap two letters in s
so the result is equal to goal, otherwise, return false. Swapping letters is
defined as taking two indices i and j (0-indexed) such that i != j and swapping
the characters at s[i] and s[j]. For example, swapping at indices 0 and 2 in
"abcd" results in "cbad".

Example 1:
Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal
to goal.

Example 2:
Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b',
which results in "ba" != goal.

Example 3:
Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa",
which is equal to goal.

Constraints:
1 <= s.length, goal.length <= 2 * 104
s and goal consist of lowercase letters."""


class Solution:
    @staticmethod
    def buddy_strings(s: str, goal: str) -> bool:
        dif_ = []
        for index, value in enumerate(s):
            if goal[index] != value:
                dif_.append(index)
        if len(dif_) != 2:
            return False
        return s[dif_[0]] == goal[dif_[1]] and s[dif_[1]] == goal[dif_[0]]


assert Solution.buddy_strings("ab", "ba")
assert not Solution.buddy_strings("", "")
assert Solution.buddy_strings("aba", "baa")
assert Solution.buddy_strings("aba", "aab")
assert not Solution.buddy_strings("abac", "bcaa")

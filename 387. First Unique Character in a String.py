"""Given a string s, find the first non-repeating character in it and return
its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
Accepted
1.3M
Submissions
2.2M
Acceptance Rate
59.0%"""
from collections import defaultdict


class Solution:
    @staticmethod
    def first_uniq_char_count(s: str) -> int:
        for index, letter in enumerate(s):
            if s.count(letter) == 1:
                return index
        return - 1

    @staticmethod
    def first_uniq_char_dict(s: str) -> int:
        count_dict = defaultdict(int)
        for letter in s:
            count_dict[letter] += 1
        for item in count_dict.items():
            if item[1] == 1:
                return s.find(item[0])
        return -1


print(Solution.first_uniq_char_dict('aabbc'))
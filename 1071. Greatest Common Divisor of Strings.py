"""For two strings s and t, we say "t divides s" if and only if s = t + ... + t
(i.e., t is concatenated with itself one or more times). Given two strings str1
and str2, return the largest string x such that x divides both str1 and str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""

Constraints:
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters."""


class Solution:
    @staticmethod
    def gcd_of_strings(str1: str, str2: str) -> str:
        short, long = (str1, str2) if len(str1) < len(str2) else (str2, str1)
        len_short = len(short)
        while len_short > 1:
            if (long.count(short[:len_short]) ==
                    len(long) / len(short[:len_short])):
                return short[:len_short]
            len_short -= 1
        return ''


assert Solution.gcd_of_strings("ABCABC", "ABC") == "ABC"
assert Solution.gcd_of_strings("ABABAB", "ABAB") == "AB"
assert Solution.gcd_of_strings("LEET", "CODE") == ""

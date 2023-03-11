"""Roman numerals are represented by seven different symbols: I, V, X, L, C, D
and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Given a roman numeral, convert it to an integer.
Input: s = "III"
Output: 3
Explanation: III = 3.

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999]."""

s1 = "III"
s2 = "LVIII"
s3 = "MCMXCIV"

IV = 4
IX = 9
XL = 40
XC = 90
CD = 400
CM = 900


class ArabianRomanConvertor:
    __roman_arabian = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
        'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
    }

    @staticmethod
    def roman_to_arabian(x):
        value = 0
        i = 0
        while i < len(x):
            if i < len(x) - 1:
                try:
                    value_complex_key = ArabianRomanConvertor.__get_arabian_by_char(x[i] + x[i + 1])
                    value += value_complex_key
                    i += 2
                except ValueError:
                    value += ArabianRomanConvertor.__get_arabian_by_char(x[i])
                    i += 1
            else:
                value += ArabianRomanConvertor.__get_arabian_by_char(x[i])
                i += 1
        return value

    @staticmethod
    def __get_arabian_by_char(char):
        if ArabianRomanConvertor.__roman_arabian.get(char) is None:
            raise ValueError("x is not Roman")
        else:
            return ArabianRomanConvertor.__roman_arabian.get(char)


print(ArabianRomanConvertor.roman_to_arabian(s3))
print(dir(ArabianRomanConvertor))

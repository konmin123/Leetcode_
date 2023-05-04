"""A valid parentheses string is either empty "", "(" + A + ")", or A + B,
where A and B are valid parentheses strings, and + represents string
concatenation. For example, "", "()", "(())()", and "(()(()))" are all valid
parentheses strings. A valid parentheses string s is primitive if it is
nonempty, and there does not exist a way to split it into s = A + B,
with A and B nonempty valid parentheses strings. Given a valid parentheses
string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk,
where Pi are primitive valid parentheses strings. Return s after removing the
outermost parentheses of every primitive string in the primitive decomposition
of s.

Example 1:
Input: s = "(()())(())"
Output: "()()()"
Explanation:
The input string is "(()())(())", with primitive decomposition "(()())" +
"(())". After removing outer parentheses of each part, this is "()()" + "()" =
"()()()".

Example 2:
Input: s = "(()())(())(()(()))"
Output: "()()()()(())"
Explanation:
The input string is "(()())(())(()(()))", with primitive decomposition "(()())"
 + "(())" + "(()(()))". After removing outer parentheses of each part, this is
 "()()" + "()" + "()(())" = "()()()()(())".

Example 3:
Input: s = "()()"
Output: ""
Explanation:
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".


Constraints:
1 <= s.length <= 105
s[i] is either '(' or ')'.
s is a valid parentheses string."""


class Solution:
    @staticmethod
    def remove_outer_par(s: str) -> str:
        open_count: int = 0
        output_list: list = []
        for element in s:
            if element == '(':
                if open_count:
                    output_list.append(element)
                open_count += 1
            else:
                if open_count > 1:
                    output_list.append(element)
                open_count -= 1
        return ''.join(output_list)


assert Solution.remove_outer_par('(()())(())') == '()()()'
assert Solution.remove_outer_par('(()())(())(()(()))') == '()()()()(())'
assert Solution.remove_outer_par('()()') == ''

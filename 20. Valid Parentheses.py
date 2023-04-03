""""Given a string s containing just the characters '(', ')', '{', '}', '['
and ']', determine if the input string is valid. An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'."""


class Solution:
    @staticmethod
    def is_valid(brackets: str) -> bool:
        queue_open_brackets: list = []
        opposite = {')': '(', ']': '[', '}': '{'}
        for bracket in brackets:
            if bracket in opposite.values():
                queue_open_brackets.append(bracket)
            else:
                if opposite[bracket] == queue_open_brackets[-1]:
                    queue_open_brackets.pop()
        return not queue_open_brackets


assert Solution.is_valid("()")
assert Solution.is_valid("()[]{}")
assert not Solution.is_valid("(]")
assert Solution.is_valid("()()()")
assert not Solution.is_valid("[(])")

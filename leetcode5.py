""""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

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

s1 = "()"
s2 = "()[]{}"
s3 = "(]"
s4 = "()()()"
s5 = "[(])"


def correct_brackets_detect(text: str) -> bool:
    list_for_open_brackets = []
    for i in text:
        if i == '(' or i == '[' or i == '{':
            list_for_open_brackets.append(i)
        if i == ')' or i == ']' or i == '}':
            if i == ')' and list_for_open_brackets[-1] == '(':
                del list_for_open_brackets[-1]
            if i == ']' and list_for_open_brackets[-1] == '[':
                del list_for_open_brackets[-1]
            if i == '}' and list_for_open_brackets[-1] == '{':
                del list_for_open_brackets[-1]
    if list_for_open_brackets:
        return False
    else:
        return True


print(correct_brackets_detect(s5))

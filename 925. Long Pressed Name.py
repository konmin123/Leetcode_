"""Your friend is typing his name into a keyboard. Sometimes, when typing a
character c, the key might get long pressed, and the character will be typed 1
or more times. You examine the typed characters of the keyboard. Return True if
it is possible that it was your friends name, with some characters
(possibly none) being long pressed.

Example 1:
Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.

Example 2:
Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it was not in the typed
output.

Constraints:
1 <= name.length, typed.length <= 1000
name and typed consist of only lowercase English letters."""


class Solution:
    @staticmethod
    def is_long_pressed_name(name: str, typed: str) -> bool:
        cur_name: int = 0
        cur_typed: int = 0
        for _ in range(len(typed)):
            if len(name) == cur_name:
                return True
            if name[cur_name] == typed[cur_typed]:
                cur_name += 1
                cur_typed += 1
            elif typed[cur_typed] == typed[cur_typed - 1]:
                cur_typed += 1
            else:
                return False
        return True


assert Solution.is_long_pressed_name("alex", "aaleex")
assert Solution.is_long_pressed_name("a", "aaaaaaa")
assert Solution.is_long_pressed_name("alex", "alex")
assert not Solution.is_long_pressed_name("saeed", "ssaaedd")

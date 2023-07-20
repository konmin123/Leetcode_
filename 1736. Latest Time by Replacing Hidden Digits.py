"""
You are given a string time in the form of  hh:mm, where some of the digits in
the string are hidden (represented by ?). The valid times are those inclusively
between 00:00 and 23:59. Return the latest valid time you can get from time
by replacing the hidden digits.

Example 1:
Input: time = "2?:?0"
Output: "23:50"
Explanation: The latest hour beginning with the digit '2' is 23 and the latest
minute ending with the digit '0' is 50.

Example 2:
Input: time = "0?:3?"
Output: "09:39"
Example 3:

Input: time = "1?:22"
Output: "19:22"


Constraints:
time is in the format hh:mm.
It is guaranteed that you can produce a valid time from the given string.
"""


class Solution:
    @staticmethod
    def maximum_time(time: str) -> str:
        new_time: list = []
        variants: dict = {0: '12', 1: '39', 3: '5', 4: '9'}
        for index, symbol in enumerate(time):
            if symbol == '?':
                volumes = variants[index]
                if len(volumes) > 1:
                    if index == 0:
                        if time[1] in ['1', '2', '3', '?']:
                            new_time.append('2')
                        else:
                            new_time.append('1')
                    else:
                        if new_time[0] == '2':
                            new_time.append('3')
                        else:
                            new_time.append('9')
                else:
                    new_time.append(volumes)
            else:
                new_time.append(symbol)
        return ''.join(new_time)


assert Solution.maximum_time('2?:?0') == '23:50'
assert Solution.maximum_time('0?:3?') == '09:39'
assert Solution.maximum_time('1?:22') == '19:22'

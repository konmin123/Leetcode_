"""Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.


Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:
-231 <= x <= 231 - 1"""
#
# x = "Я иду с мечем судия"
# # Как решить без str
#
# def palindrom(x):
#     x = str(x)
#     palindrome_ = True
#     for i in range(int((len(str(x)))/2)):
#         if x[i] != x[-i - 1]:
#             palindrome_ = False
#             break
#     return print(palindrome_)
#
#
# palindrom(x)

x = 121

# через деление от ста и меньше.
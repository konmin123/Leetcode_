"""You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order, and each of their nodes
contains a single digit. Add the two numbers and return the sum as a linked
list. You may assume the two numbers do not contain any leading zero, except
the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading
zeros."""
from typing import Optional as Opt


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def add_two_numbers(l1: Opt[ListNode], l2: Opt[ListNode]) -> Opt[ListNode]:
        first_number = ''
        second_number = ''
        while l1:
            first_number = str(l1.val) + first_number
            l1 = l1.next
        while l2:
            second_number = str(l2.val) + second_number
            l2 = l2.next
        third_number = str(int(first_number) + int(second_number))[::-1]
        l3 = ListNode()
        current_node = l3
        for string_digit in third_number.split():
            current_node.val = int(string_digit)
            current_node = current_node.next
        return l3


f3 = ListNode(3)
f2 = ListNode(4, f3)
f1 = ListNode(2, f2)

s3 = ListNode(4)
s2 = ListNode(6, s3)
s1 = ListNode(5, s2)

t = Solution.add_two_numbers(f1, s1)
while t:
    print(t.val)
    t = t.next

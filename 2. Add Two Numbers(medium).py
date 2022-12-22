"""You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order, and each of their nodes
contains a single digit. Add the two numbers and return the sum as a linked
list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

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
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def add_two_numbers(l1: Optional[ListNode],
                        l2: Optional[ListNode]) -> Optional[ListNode]:
        cur_node_1 = l1
        cur_node_2 = l2
        over_value = (cur_node_1.val + cur_node_2.val) // 10
        head = ListNode((cur_node_1.val + cur_node_2.val) % 10)
        new_node = head
        prev_new_node = head
        while cur_node_1.next or cur_node_2.next:
            if cur_node_1.next and cur_node_2.next:
                cur_node_1 = cur_node_1.next
                cur_node_2 = cur_node_2.next
                new_node = ListNode(
                    (cur_node_1.val + cur_node_2.val + over_value) % 10
                )
                over_value = (cur_node_1.val + cur_node_2.val) // 10
            elif cur_node_1.next:
                cur_node_1 = cur_node_1.next
                new_node = ListNode((cur_node_1.val + over_value) % 10)
            elif cur_node_2.next:
                cur_node_2 = cur_node_2.next
                new_node = ListNode((cur_node_2.val + over_value) % 10)
            prev_new_node.next = new_node
            prev_new_node = new_node
        if over_value:
            new_node = ListNode(1)
            prev_new_node.next = new_node
        return head


if __name__ == '__main__':
    a = ListNode(9)
    p = ListNode(9, a)
    o = ListNode(9, p)
    i = ListNode(9, o)
    u = ListNode(9)
    y = ListNode(9, u)
    t = ListNode(9, y)
    r = ListNode(9, t)
    e = ListNode(9, r)
    w = ListNode(9, e)
    q = ListNode(9, w)
    l1 = q
    l2 = i
    x = Solution.add_two_numbers(l1, l2)
    while x:
        print(x.val)
        x = x.next


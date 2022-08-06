"""Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []

Constraints:

    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

    @staticmethod
    def init_linked_list(seq):
        prev = None
        for value in seq[::-1]:
            if not prev:
                prev = ListNode(val=value)
            else:
                prev = ListNode(val=value, next_=prev)
        return prev


class Solution:
    @staticmethod
    def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        prev = None
        while current_node:
            next_node = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next_node
        return prev

    @staticmethod
    def val_linked_list(head: Optional[ListNode]) -> list:
        current_node = head
        list_values = []
        while current_node:
            list_values.append(current_node.val)
            current_node = current_node.next
        return list_values


if __name__ == '__main__':
    z = ListNode.init_linked_list([3, 2, 1])
    print(Solution.val_linked_list(z))
    z = Solution.reverse_list(z)
    print(Solution.val_linked_list(z))

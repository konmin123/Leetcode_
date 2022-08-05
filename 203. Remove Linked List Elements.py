"""Given the head of a linked list and an integer val,
remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1:

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:

Input: head = [], val = 1
Output: []

Example 3:

Input: head = [7,7,7,7], val = 7
Output: []

Constraints:

    The number of nodes in the list is in the range [0, 104].
    1 <= Node.val <= 50
    0 <= val <= 50

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


head_list_nodes = ListNode.init_linked_list([1, 2, 3, 4, 5, 6])


class Solution:
    @staticmethod
    def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
        current_node = head
        next_node = None
        prev_node = None
        while current_node:
            next_node = current_node.next
            if not prev_node and current_node.val == val:
                head = current_node.next
                current_node.next = None
            if prev_node and current_node.val == val:
                prev_node.next = next_node
            if not next_node and current_node.val == val:
                prev_node.next = None
            prev_node = current_node
            current_node = next_node
        return head

    @staticmethod
    def val_linked_list(head: Optional[ListNode]) -> list:
        current_node = head
        list_values = []
        while current_node:
            list_values.append(current_node.val)
            current_node = current_node.next
        return list_values


if __name__ == '__main__':
    head_list_nodes = Solution.remove_elements(head_list_nodes, 5)
    print(Solution.val_linked_list(head_list_nodes))
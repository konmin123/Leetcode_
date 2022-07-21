"""Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
 Return the linked list sorted as well.

Example 1:

Input: head = [1,1,2]
Output: [1,2]

Example 2:

Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:

    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.

"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)


class Solution:
    @staticmethod
    def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        else:
            current_node_uniq = head
            current_node = head
            while current_node.next:
                current_node = current_node.next
                if current_node_uniq.val != current_node.val:
                    current_node_uniq.next = current_node
                    current_node_uniq = current_node
            node_for_print = head
            while node_for_print:
                print(node_for_print.val)
                node_for_print = node_for_print.next


if __name__ == '__main__':
    Solution.delete_duplicates(node1)
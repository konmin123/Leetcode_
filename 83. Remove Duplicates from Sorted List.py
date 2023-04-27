"""Given the head of a sorted linked list, delete all duplicates such that each
element appears only once. Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order."""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next_ = next_


node5 = ListNode(3)
node4 = ListNode(2, node5)
node3 = ListNode(1, node4)
node2 = ListNode(1, node3)
node1 = ListNode(1, node2)

test_node_3 = ListNode(3)
test_node_2 = ListNode(2, test_node_3)
test_node = ListNode(1, test_node_2)


class Solution:
    @staticmethod
    def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            prev_node = head
            cur_node = head.next_
            while cur_node:
                if prev_node.val == cur_node.val:
                    cur_node = cur_node.next_zero_index
                    prev_node.next_ = cur_node
                else:
                    prev_node = cur_node
                    cur_node = cur_node.next_zero_index
        return head

    @staticmethod
    def values_ll(head: ListNode) -> list:
        data = [head.val]
        cur = head
        while cur.next_:
            cur = cur.next_
            data.append(cur.val)
        return data


assert Solution.values_ll(
    Solution.delete_duplicates(node1)) == Solution.values_ll(test_node)

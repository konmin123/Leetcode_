"""Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following
the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Constraints:

    The number of the nodes in the list is in the range [0, 104].
    -105 <= Node.val <= 105
    pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""
from typing import Optional


class ListNode:
    def __init__(self, val, next_=None):
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

    @staticmethod
    def init_cycle_for_linked_list(head, pos: int):
        current_node = head
        pos_node = None
        count = 1
        while True:
            if current_node.next is None:
                current_node.next = pos_node
                break
            if count == pos:
                pos_node = current_node
            current_node = current_node.next
            count +=1
        return head

    @staticmethod
    def print_value_linked_list(head):
        count = 1
        current_node = head
        while count < 15:
            print(current_node.val)
            current_node = current_node.next
            count += 1
            if current_node is None:
                break


class Solution:

    @staticmethod
    def has_cycle(head: Optional[ListNode]) -> bool:
        temp1 = head
        temp2 = head
        while temp1.next and temp2.next and temp2.next.next:
            temp1 = temp1.next
            temp2 = temp2.next.next
            if temp1 == temp2:
                return True
        return False


if __name__ == '__main__':
    z = ListNode.init_linked_list([1, 2])
    print(z)
    ListNode.init_cycle_for_linked_list(z, 1)
    ListNode.print_value_linked_list(z)
    print(Solution.has_cycle(z))


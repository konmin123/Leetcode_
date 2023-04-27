"""Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false


Constraints:

    The number of nodes in the list is in the range [1, 105].
    0 <= Node.val <= 9


Follow up: Could you do it in O(n) time and O(1) space?"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next_ = next_


class Solution:
    @staticmethod
    def is_palindrome(head: Optional[ListNode]) -> bool:
        slow_cursor = head
        fast_cursor = head
        while fast_cursor and fast_cursor.next_:
            slow_cursor = slow_cursor.next_
            fast_cursor = fast_cursor.next_.next_zero_index
        prev_node = slow_cursor
        slow_cursor = slow_cursor.next_
        prev_node.next_ = None
        while slow_cursor:
            next_node = slow_cursor.next_zero_index
            slow_cursor.next_zero_index = prev_node
            prev_node = slow_cursor
            slow_cursor = next_node
        fast_cursor = head
        slow_cursor = prev_node
        while slow_cursor:
            if fast_cursor.val == slow_cursor.val:
                fast_cursor = fast_cursor.next_
                slow_cursor = slow_cursor.next_
            else:
                return False
        return True


if __name__ == '__main__':
    sixth = ListNode(1)
    fifth = ListNode(2, sixth)
    fourth = ListNode(3, fifth)
    third = ListNode(3, fourth)
    second = ListNode(2, third)
    first = ListNode(1, second)

    print(Solution.is_palindrome(first))



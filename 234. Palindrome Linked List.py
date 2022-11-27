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
        current_node = head
        my_stack = list()
        count_in_stack = 0
        while current_node:
            if count_in_stack == 0:
                my_stack.append(current_node.val)
                count_in_stack += 1
            else:
                if my_stack[-1] == current_node.val:
                    my_stack.pop()
                    count_in_stack -= 1
                else:
                    my_stack.append(current_node.val)
                    count_in_stack += 1
            current_node = current_node.next_
        return bool(not my_stack)


if __name__ == '__main__':
    sixth = ListNode(1)
    fifth = ListNode(2, sixth)
    fourth = ListNode(3, fifth)
    third = ListNode(3, fourth)
    second = ListNode(2, third)
    first = ListNode(1, second)

    print(Solution.is_palindrome(first))
    print(Solution. is_palindrome(third))
    print(Solution.is_palindrome(ListNode()))



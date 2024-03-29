"""Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

    intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
    listA - The first linked list.
    listB - The second linked list.
    skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
    skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.

The judge will then create the linked structure based on these inputs and pass the two heads,
headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.

Example 1:

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5].
There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

Example 2:

Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4].
There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

Example 3:

Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5].
Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.

Constraints:

    The number of nodes of listA is in the m.
    The number of nodes of listB is in the n.
    1 <= m, n <= 3 * 104
    1 <= Node.val <= 105
    0 <= skipA < m
    0 <= skipB < n
    intersectVal is 0 if listA and listB do not intersect.
    intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.

Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?"""
from typing import Optional


class ListNode:
    def __init__(self, x, next_=None):
        self.val = x
        self.next = next_


# class Linked_list:
#     @staticmethod
#     def new_list(head):

node_b3 = ListNode(4)
node_b2 = ListNode(2, node_b3)
node_b1 = ListNode(3, node_b2)


node_a4 = ListNode(2, node_b3)
node_a3 = ListNode(1, node_a4)
node_a2 = ListNode(9, node_a3)
node_a1 = ListNode(1, node_a2)


class Solution:
    @staticmethod
    def get_intersection_node(head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:  # brute force O(n**2), O(1)
        current_node_a = head_a
        current_node_b = head_b
        while current_node_a:
            while current_node_b:
                if current_node_a.val == current_node_b.val and current_node_a.next == current_node_b.next:
                    return current_node_a.val
                else:
                    current_node_b = current_node_b.next
            current_node_a = current_node_a.next
            current_node_b = head_b

    @staticmethod
    def get_intersection_node_2(head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:  # hash dict, O(n), O(n/2)
        dict_val_1 = {}
        current_node_a = head_a
        current_node_b = head_b
        index = 0
        while current_node_a:
            dict_val_1[index] = current_node_a.val
            current_node_a = current_node_a.next
            index += 1
        while current_node_b:
            if current_node_b.val in dict_val_1.values():
                return current_node_b.val
            else:
                current_node_b = current_node_b.next
        return None


if __name__ == '__main__':
    print(Solution.get_intersection_node_2(node_a1, node_b1))
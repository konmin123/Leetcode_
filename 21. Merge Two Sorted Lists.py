"""You are given the heads of two sorted linked lists list1 and list2. Merge
the two lists in a one sorted list. The list should be made by splicing
together the nodes of the first two lists.Return the head of the merged linked
list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order."""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next_ = next_


class Solution:
    @staticmethod
    def merge_two_lists(list1: Optional[ListNode],
                        list2: Optional[ListNode]) -> Optional[ListNode]:
        if isinstance(list1, ListNode) and isinstance(list2, ListNode):
            head = ListNode()
            cur_node = head
            while isinstance(list1, ListNode) and isinstance(list2, ListNode):
                if list1.val < list2.val:
                    cur_node.val = list1.val
                    list1 = list1.next_
                else:
                    cur_node.val = list2.val
                    list2 = list2.next_
                cur_node.next_ = ListNode()
                cur_node = cur_node.next_
            if list1:
                cur_node.val = list1.val
                cur_node.next_ = list1.next_
            else:
                cur_node.val = list2.val
                cur_node.next_ = list2.next_
            return head
        elif isinstance(list1, ListNode):
            return list1
        else:
            return list2

    @staticmethod
    def check_list(node: ListNode):
        cur = node
        list_values = []
        while cur:
            list_values.append(cur.val)
            cur = cur.next_
        return list_values


first_list_2 = ListNode(4)
first_list_1 = ListNode(2, first_list_2)
first_list_head = ListNode(1, first_list_1)

second_list_2 = ListNode(4)
second_list_1 = ListNode(3, second_list_2)
second_list_head = ListNode(1, second_list_1)

merge_list_5 = ListNode(4)
merge_list_4 = ListNode(4, merge_list_5)
merge_list_3 = ListNode(3, merge_list_4)
merge_list_2 = ListNode(2, merge_list_3)
merge_list_1 = ListNode(1, merge_list_2)
merge_list_head = ListNode(1, merge_list_1)


assert Solution.check_list(merge_list_head) == Solution.check_list(
    Solution.merge_two_lists(first_list_head, second_list_head))

"""You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []

Constraints:

    k == lists.length
    0 <= k <= 104
    0 <= lists[i].length <= 500
    -104 <= lists[i][j] <= 104
    lists[i] is sorted in ascending order.
    The sum of lists[i].length will not exceed 104.
"""
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

    @staticmethod
    def init_k_ll(k=1, len_=1) -> list:
        list_of_heads = []
        if k >= 1:
            for head in range(k):
                current_node = ListNode(1)
                list_of_heads.append(current_node)
                if len_ > 1:
                    for value in range(2, len_ + 1):
                        next_node = ListNode(value)
                        current_node.next = next_node
                        current_node = next_node
        return list_of_heads


class Solution:
    @staticmethod
    def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dict_values = {}
        for head in lists:
            current_node = head
            while current_node:
                if current_node.val in dict_values:
                    dict_values[current_node.val] += 1
                    current_node = current_node.next
                else:
                    dict_values[current_node.val] = 1
                    current_node = current_node.next
        if dict_values:
            head = ListNode(min(dict_values))
            current_node = head
            dict_values[min(dict_values)] -= 1
            for key in dict_values:
                while dict_values[key] > 0:
                    current_node.next = ListNode(key)
                    current_node = current_node.next
                    dict_values[key] -= 1
            return head


if __name__ == '__main__':
    x = ListNode.init_k_ll(1, 1)
    print(Solution.merge_k_lists(x))

"""21. Merge Two Sorted Lists
Easy

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



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
    Both list1 and list2 are sorted in non-decreasing order.

"""
from typing import List

list_1 = [1, 2, 4]
list_2 = [2, 3, 6, 7]


def merge_two_sorted_lists(first_list: List[int], second_list: List[int]) -> List[int]:
    i = 0
    j = 0
    output = []
    if not first_list or not second_list:
        output.extend(first_list)
        output.extend(second_list)
    else:
        while len(output) < len(first_list) + len(second_list):
            if first_list[i] <= second_list[j]:
                output.append(first_list[i])
                i += 1
            else:
                output.append(second_list[j])
                j += 1
            if i == len(first_list):
                output.extend(second_list[j:])
                break
            if j == len(second_list):
                output.extend(first_list[i:])
                break
    return output


if __name__ == '__main__':
    print(merge_two_sorted_lists(list_1, list_2))

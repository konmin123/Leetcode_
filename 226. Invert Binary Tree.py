"""Given the root of a binary tree, invert the tree, and return its root.

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:

Input: root = [2,1,3]
Output: [2,3,1]
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def converter(sequence: list) -> TreeNode:
        root = TreeNode(sequence[0])
        list_for_links = [root]
        list_new_nodes = []
        current_index = 1
        while current_index < len(sequence):    # Пока индекс значения для создания ноды корректный - продолжаем
            for i in range(2 * len(list_for_links)):  # Мы тут создаём список новых нод
                value_for_new_node = sequence[current_index]
                print(value_for_new_node, current_index)
                if value_for_new_node:
                    list_new_nodes.append(TreeNode(value_for_new_node))
                else:
                    list_new_nodes.append(None)
                current_index += 1
            count_for_link = 0
            for node in list_for_links:  # Тут мы связываем ноды
                if node is TreeNode:
                    node.left = list_new_nodes[count_for_link]
                    count_for_link += 1
                    node.right = list_new_nodes[count_for_link]
                    count_for_link += 1
                else:
                    count_for_link += 2
            print(list_for_links, list_new_nodes)
            list_for_links = list_new_nodes
            list_new_nodes = []

        return root


if __name__ == '__main__':
    s = Solution.converter([10, None, 15, None, None, 13, None])







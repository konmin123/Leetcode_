"""94. Binary Tree Inorder Traversal
Easy

Given the root of a binary tree, return the inorder traversal of its nodes' values.



Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [1]
Output: [1]



Constraints:

    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively?"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node2 = TreeNode(2)
node1 = TreeNode(1, None, node2)
node4 = TreeNode(4)
node3 = TreeNode(3, node1, node4)
node8 = TreeNode(8)
node6 = TreeNode(6, node3, node8)
node19 = TreeNode(19)
node21 = TreeNode(21)
node20 = TreeNode(20, node19, node21)
node16 = TreeNode(16)
node17 = TreeNode(17, node16, node20)
node9 = TreeNode(9, node6, node17)
root = node9


class Solution:
    @staticmethod
    def inorder_traversal_1(root_: Optional[TreeNode]) -> List[int]:
        """Обход дерева в ширину"""
        output_list = []
        queue = [root_]
        for node in queue:
            output_list.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return output_list

    @staticmethod
    def inorder_traversal_2(root_: Optional[TreeNode]) -> List[int]:
        """Обход дерева в глубину"""
        output_list = []
        queue_left = [root_]
        queue_right = []
        while queue_left or queue_right:
            if queue_left:
                current_node = queue_left[0]
                queue_left.pop(0)
            elif queue_right:
                current_node = queue_right[0]
                queue_right.pop(0)
            else:
                return output_list
            output_list.append(current_node.val)
            if current_node.left:
                queue_left.append(current_node.left)
            if current_node.right:
                queue_right.insert(0, current_node.right)
        return output_list

    @staticmethod
    def inorder_traversal_3(root_: Optional[TreeNode]) -> List[int]:
        """Рекурсивный обход в глубину"""

        if not root_:
            return []
        if not (root_.left or root_.right):
            return [root_.val]

        left = Solution.inorder_traversal_3(root_.left) if root_.left else []

        right = Solution.inorder_traversal_3(root_.right) if root_.right else []

        return [root_.val] + left + right


if __name__ == '__main__':
    print(Solution.inorder_traversal_2(root))


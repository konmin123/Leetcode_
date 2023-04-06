"""Given the roots of two binary trees p and q, write a function to check if
they are the same or not. Two binary trees are considered the same if they are
structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:
The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        output_list = [[], []]
        queue = [[p], [q]]
        for index in range(2):
            for node in queue[index]:
                output_list[index].append(node.val)
                if node.left:
                    queue[index].append(node.left)
                if node.right:
                    queue[index].append(node.right)
        if output_list[0] == output_list[1]:
            return True
        else:
            return False

    @staticmethod
    def is_same_tree_rec(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """Рекурсивное сравнение деревьев"""
        def inorder_traversal_3(root_: Optional[TreeNode]) -> List[int]:
            if not root_:
                return []
            if not (root_.left or root_.right):
                return [root_.val]

            left = inorder_traversal_3(root_.left) if root_.left else []

            right = inorder_traversal_3(root_.right) if root_.right else []

            return [root_.val] + left + right

        if inorder_traversal_3(p) == inorder_traversal_3(q):
            return True
        else:
            return False


node8_1 = TreeNode(8)
node6_1 = TreeNode(6)
node7_1 = TreeNode(7, node6_1, node8_1)
root1 = node7_1

node8_2 = TreeNode(8)
node6_2 = TreeNode(6)
node7_2 = TreeNode(7, node6_2, node8_2)
root2 = node7_2

node8_3 = TreeNode(9)
node6_3 = TreeNode(6)
node7_3 = TreeNode(7, node6_3, node8_3)
root3 = node7_3

assert Solution.is_same_tree(root1, root2)
assert not Solution.is_same_tree(root1, root3)
assert Solution.is_same_tree_rec(root1, root2)
assert not Solution.is_same_tree_rec(root1, root3)

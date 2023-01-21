"""Given the root of a binary tree, return the length of the diameter of the
tree.

The diameter of a binary tree is the length of the longest path between any
two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges
between them.

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1

Constraints:
The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
        def node_depth(node, depth=0):
            if node.left and node.right:
                return max(node_depth(node.left, depth + 1),
                           node_depth(node.right, depth + 1))
            if node.left:
                return node_depth(node.left, depth + 1)
            if node.right:
                return node_depth(node.right, depth + 1)
            return 1 + depth
        if root.left and root.right:
            return node_depth(root.left) + node_depth(root.right) + 1
        if root.left:
            return node_depth(root.left)
        if root.right:
            return node_depth(root.right)
        return 0


node_1_5 = TreeNode(5)
node_1_4 = TreeNode(4)
node_1_3 = TreeNode(3)
node_1_2 = TreeNode(2, node_1_4, node_1_5)
root_1 = TreeNode(1, node_1_2, node_1_3)

node_2_2 = TreeNode(2)
root_2 = TreeNode(1, node_2_2)

root_3 = TreeNode(1)

assert Solution.diameter_of_binary_tree(root_1) == 4
assert Solution.diameter_of_binary_tree(root_2) == 1
assert Solution.diameter_of_binary_tree(root_3) == 0

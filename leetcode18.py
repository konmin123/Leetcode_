"""Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

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
    -104 <= Node.val <= 104

"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node8_1 = TreeNode(8)
node6_1 = TreeNode(6)
node7_1 = TreeNode(7, node6_1, node8_1)
root1 = node7_1

node8_2 = TreeNode(8)
node6_2 = TreeNode(6)
node7_2 = TreeNode(7, node6_2, node8_2)
root2 = node7_2


class Solution:
    @staticmethod
    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        output_1 = []
        output_2 = []
        
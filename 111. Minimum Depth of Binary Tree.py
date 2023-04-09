"""Given a binary tree, find its minimum depth. The minimum depth is the number
of nodes along the shortest path from the root node down to the nearest leaf
node. Note: A leaf is a node with no children.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

Constraints:
The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def min_depth(root: Optional[TreeNode]) -> int:
        depth = 0
        if isinstance(root, TreeNode):
            node_queue = [root]
            next_level = []
            while node_queue:
                depth += 1
                for node in node_queue:
                    if node.left or node.right:
                        if node.left:
                            next_level.append(node.left)
                        if node.right:
                            next_level.append(node.right)
                    else:
                        return depth
                node_queue, next_level = next_level, []
        return depth


node_1_5 = TreeNode(7)
node_1_4 = TreeNode(15)
node_1_3 = TreeNode(20, node_1_4, node_1_5)
node_1_2 = TreeNode(9)
root_1 = TreeNode(3, node_1_2, node_1_3)

node_2_7 = TreeNode(4)
node_2_6 = TreeNode(4)
node_2_5 = TreeNode(3)
node_2_4 = TreeNode(3, node_2_6, node_2_7)
node_2_3 = TreeNode(2)
node_2_2 = TreeNode(2, node_2_4, node_2_5)
root_2 = TreeNode(1, node_2_2, node_2_3)

root_3 = TreeNode(12)


assert Solution.min_depth(root_1) == 2
assert Solution.min_depth(root_2) == 2
assert Solution.min_depth(root_3) == 1
assert Solution.min_depth(None) == 0

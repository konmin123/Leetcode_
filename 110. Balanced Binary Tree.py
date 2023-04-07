"""Given a binary tree, determine if it is height-balanced.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def is_balanced(root_: Optional[TreeNode]) -> bool:
        queue = [root_]
        for node in queue:
            left = 0
            right = 0
            if node.left:
                left = Solution.node_depth(node.left)
                queue.append(node.left)
            if node.right:
                right = Solution.node_depth(node.right)
                queue.append(node.right)
            if abs(left - right) > 1:
                return False
        return True

    @staticmethod
    def node_depth(node: Optional[TreeNode]):
        queue_ = [node]
        next_level = []
        depth = 0
        while queue_:
            for node in queue_:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            depth += 1
            queue_ = next_level
            next_level = []
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

assert Solution.is_balanced(root_1)
assert not Solution.is_balanced(root_2)

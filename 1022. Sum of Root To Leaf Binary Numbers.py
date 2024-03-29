"""You are given the root of a binary tree where each node has a value 0 or 1.
Each root-to-leaf path represents a binary number starting with the most
significant bit. For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this
could represent 01101 in binary, which is 13. For all leaves in the tree,
consider the numbers represented by the path from the root to that leaf.
Return the sum of these numbers. The test cases are generated so that the
answer fits in a 32-bits integer.

Example 1:
Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

Example 2:
Input: root = [0]
Output: 0

Constraints:
The number of nodes in the tree is in the range [1, 1000].
Node.val is 0 or 1."""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def sum_root_to_leaf(root: Optional[TreeNode]) -> int:
        result = 0
        stack = [(root, "")]

        while (stack):
            node, path = stack.pop()
            if node:
                path += str(node.val)

                if not (node.left or node.right):
                    result += int(path, 2)
                else:
                    stack.append((node.left, path))
                    stack.append((node.right, path))
        return result


node_1_7 = TreeNode(1)
node_1_6 = TreeNode(0)
node_1_5 = TreeNode(1)
node_1_4 = TreeNode(0)
node_1_3 = TreeNode(1, node_1_6, node_1_7)
node_1_2 = TreeNode(0, node_1_4, node_1_5)
node_1 = TreeNode(1, node_1_2, node_1_3)
node_2 = TreeNode(0)


assert Solution.sum_root_to_leaf(node_1) == 22
assert Solution.sum_root_to_leaf(node_2) == 0





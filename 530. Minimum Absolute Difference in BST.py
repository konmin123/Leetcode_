"""Given the root of a Binary Search Tree (BST), return the minimum absolute
difference between the values of any two different nodes in the tree.

Example 1:
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1

Constraints:
The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105"""
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def get_minimum_difference(root: Optional[TreeNode]) -> int:
        queue: deque = deque()
        queue.append(root)
        dif_val: int = 106
        while queue:
            cur_node = queue.pop()
            if isinstance(cur_node, TreeNode):
                if cur_node.right:
                    queue.append(cur_node.right)
                    if cur_node.right.val - cur_node.val < dif_val:
                        dif_val = cur_node.right.val - cur_node.val
                if cur_node.left:
                    queue.append(cur_node.left)
                    if cur_node.val - cur_node.left.val < dif_val:
                        dif_val = cur_node.val - cur_node.left.val
        if dif_val == 106:
            return 0
        return dif_val


node_3_1 = TreeNode(3)
node_1_1 = TreeNode(1)
node_6_1 = TreeNode(6)
node_2_1 = TreeNode(2, node_1_1, node_3_1)
root_1 = TreeNode(4, node_2_1, node_6_1)

node_49_2 = TreeNode(49)
node_12_2 = TreeNode(12)
node_48_2 = TreeNode(48, node_12_2, node_49_2)
node_0_2 = TreeNode(0)
root_2 = TreeNode(1, node_0_2, node_48_2)

root_3 = TreeNode(1)

assert Solution.get_minimum_difference(root_1) == 1
assert Solution.get_minimum_difference(root_2) == 1
assert Solution.get_minimum_difference(root_3) == 0



"""Given the root of a binary tree, return the sum of all left leaves.
A leaf is a node with no children. A left leaf is a leaf that is the left
child of another node.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15
respectively.

Example 2:
Input: root = [1]
Output: 0

Constraints:
The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def sum_of_left_leaves(root: Optional[TreeNode]) -> int:
        deque = [root]
        sum_left_nodes = 0
        while deque:
            current_node = deque.pop()
            if current_node.left:
                deque.append(current_node.left)
                sum_left_nodes += current_node.left.val
            if current_node.right:
                deque.append(current_node.right)
        return sum_left_nodes


if __name__ == '__main__':
    tree_node5 = TreeNode(val=7)
    tree_node4 = TreeNode(val=15)
    tree_node3 = TreeNode(val=20, left=tree_node4, right=tree_node5)
    tree_node2 = TreeNode(val=9)
    tree_root = TreeNode(val=3, left=tree_node2, right=tree_node3)
    print(Solution.sum_of_left_leaves(tree_root))

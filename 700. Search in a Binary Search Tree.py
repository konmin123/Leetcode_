"""You are given the root of a binary search tree (BST) and an integer val.
Find the node in the BST that the node's value equals val and return the
subtree rooted with that node. If such a node does not exist, return null.

Example 1:
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Example 2:
Input: root = [4,2,7,1,3], val = 5
Output: []

Constraints:
The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 107
root is a binary search tree.
1 <= val <= 107
Accepted
608K
Submissions
784.7K
Acceptance Rate
77.5%"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def search_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root.val == val:
            return root
        elif root.val > val:
            if root.left:
                return Solution.search_bst(root.left, val)
        elif root.val < val:
            if root.right:
                return Solution.search_bst(root.right, val)
        return None


node_1_3 = TreeNode(3)
node_1_1 = TreeNode(1)
node_1_7 = TreeNode(7)
node_1_2 = TreeNode(2, node_1_1, node_1_3)
root_1 = TreeNode(4, node_1_2, node_1_7)


assert Solution.search_bst(root_1, 2) == node_1_2
assert not Solution.search_bst(root_1, 5)



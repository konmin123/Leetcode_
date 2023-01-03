"""Given the root of a binary search tree (BST) with duplicates, return all the
mode(s) (i.e., the most frequently occurred element) in it.
If the tree has more than one mode, return them in any order.
Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than or equal to
the node's key.
The right subtree of a node contains only nodes with keys greater than or equal
to the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:

Input: root = [1,null,2,2]
Output: [2]

Example 2:
Input: root = [0]
Output: [0]

Constraints:
The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105

Follow up: Could you do that without using any extra space? (Assume that the
implicit stack space incurred due to recursion does not count)."""
from collections import defaultdict
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def find_mode(root: Optional[TreeNode]) -> List[int]:
        node_values = defaultdict(int)
        queue = [root]
        next_level_queue = []
        while queue:
            for node in queue:
                node_values[node.val] += 1
                if node.left:
                    next_level_queue.append(node.left)
                if node.right:
                    next_level_queue.append(node.right)
            queue = next_level_queue
            next_level_queue = []
        return [x[0] for x in node_values.items()
                if x[1] == max(node_values.values())]

    @staticmethod
    def find_mode_rec(root: Optional[TreeNode]) -> List[int]:
        if root.val == 0:
            return [0]
        count_values = defaultdict(int)
        if type(root) is TreeNode:
            Solution.for_rec(root, count_values)
        return [x[0] for x in count_values.items()
                if x[1] == max(count_values.values())]

    @staticmethod
    def for_rec(node: TreeNode, count_values: defaultdict) -> defaultdict:
        count_values[node.val] += 1
        if node.left:
            Solution.for_rec(node.left, count_values)
        if node.right:
            Solution.for_rec(node.right, count_values)
        else:
            return count_values


node_for_test_root_2 = TreeNode(2)
node_for_test_root_1 = TreeNode(2, left=node_for_test_root_2)
root_for_test_one = TreeNode(1, left=None, right=node_for_test_root_1)

root_for_test_two = TreeNode(0)

assert Solution.find_mode(root_for_test_one) == [2]
assert Solution.find_mode(root_for_test_two) == [0]
assert Solution.find_mode_rec(root_for_test_one) == [2]
assert Solution.find_mode_rec(root_for_test_two) == [0]

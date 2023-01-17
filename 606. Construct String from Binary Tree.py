"""Given the root of a binary tree, construct a string consisting of
parenthesis and integers from a binary tree with the preorder traversal way,
and return it.
Omit all the empty parenthesis pairs that do not affect the one-to-one mapping
relationship between the string and the original binary tree.

Example 1:
Input: root = [1,2,3,4]
Output: "1(2(4))(3)"
Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to
omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"

Example 2:
Input: root = [1,2,3,null,4]
Output: "1(2()(4))(3)"
Explanation: Almost the same as the first example, except we cannot omit the
first parenthesis pair to break the one-to-one mapping relationship between
the input and the output.

Constraints:
The number of nodes in the tree is in the range [1, 104].
-1000 <= Node.val <= 1000"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node_1_4 = TreeNode(4)
node_1_3 = TreeNode(3)
node_1_2 = TreeNode(2, node_1_4)
root_1 = TreeNode(1, node_1_2, node_1_3)

node_2_4 = TreeNode(4)
node_2_3 = TreeNode(3)
node_2_2 = TreeNode(2, None, node_2_4)
root_2 = TreeNode(1, node_2_2, node_2_3)

root_3 = TreeNode(1)


class Solution:
    @staticmethod
    def tree2str(root: Optional[TreeNode]) -> str:
        return Solution.str_node(root)

    @staticmethod
    def str_node(node: TreeNode):
        if node.left and node.right:
            return (str(node.val) + '(' + Solution.str_node(node.left) + ')('
                    + Solution.str_node(node.right) + ')')
        elif node.left:
            return str(node.val) + '(' + Solution.str_node(node.left) + ')'
        elif node.right:
            return str(node.val) + '()(' + Solution.str_node(node.right) + ')'
        return str(node.val)


assert Solution.tree2str(root_1) == "1(2(4))(3)"
assert Solution.tree2str(root_2) == "1(2()(4))(3)"
assert Solution.tree2str(root_3) == "1"

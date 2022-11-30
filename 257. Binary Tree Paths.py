"""Given the root of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children.
Example 1:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
Example 2:
Input: root = [1]
Output: ["1"]
Constraints:
The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def binary_tree_paths(root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        current_stack = [('', root)]
        next_stack = []
        output_list = []
        while current_stack:
            current_tuple = current_stack.pop()
            current_text = current_tuple[0]
            current_node = current_tuple[1]
            if current_node.left:
                next_stack.append((current_text + str(current_node.val) + '->', current_node.left))
            if current_node.right:
                next_stack.append((current_text + str(current_node.val) + '->', current_node.right))
            if not current_node.left and not current_node.right:
                output_list.append(current_text + str(current_node.val))
            if not current_stack:
                current_stack = next_stack
                next_stack = []
        output_list.reverse()
        return output_list


if __name__ == '__main__':
    tree_node4 = TreeNode(val=3)
    tree_node3 = TreeNode(val=5)
    tree_node2 = TreeNode(val=2, left=None, right=tree_node3)
    tree_root = TreeNode(val=1, left=tree_node2, right=tree_node4)
    print(Solution.binary_tree_paths(None))


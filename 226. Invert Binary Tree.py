"""Given the root of a binary tree, invert the tree, and return its root.

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:

Input: root = [2,1,3]
Output: [2,3,1]
"""

from tree_creator import Tree


class Solution:
    @staticmethod
    def rev_tree(tree: Tree):
        next_nodes = [tree.root]
        for node in next_nodes:
            if node is not None:
                next_nodes.append(node.left)
                next_nodes.append(node.right)
                node.left, node.right = node.right, node.left


if __name__ == '__main__':
    s = Tree([2, 1, 3])
    Solution.rev_tree(s)
    print(s.list_values_tree())


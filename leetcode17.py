"""94. Binary Tree Inorder Traversal
Easy

Given the root of a binary tree, return the inorder traversal of its nodes' values.



Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [1]
Output: [1]



Constraints:

    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively?"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # def __str__(self):
    #     return f'TreeNode()'


node2 = TreeNode(2)
node1 = TreeNode(1, None, node2)
node4 = TreeNode(4)
node3 = TreeNode(3, node1, node4)
node8 = TreeNode(8)
node6 = TreeNode(6, node3, node8)
node19 = TreeNode(19)
node21 = TreeNode(21)
node20 = TreeNode(20, node19, node21)
node16 = TreeNode(16)
node17 = TreeNode(17, node16, node20)
node9 = TreeNode(9, node6, node17)
root = node9

print(root)


class Solution:
    @staticmethod
    def inorder_traversal(root_: Optional[TreeNode]) -> List[int]:
        output_list = []
        queue = [root_]
        for node in queue:
            output_list.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return output_list


if __name__ == '__main__':
    print(Solution.inorder_traversal(root))


"""Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    -100 <= Node.val <= 100

Follow up: Could you solve it both recursively and iteratively?"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node4_r = TreeNode(4)
node4_l = TreeNode(4)
node3_r = TreeNode(3)
node3_l = TreeNode(3)
node2_l = TreeNode(2, node3_l, node4_l)
node2_r = TreeNode(2, node4_r, node3_r)
node1 = TreeNode(1, node2_l, node2_r)
root_ = node1


class Solution:
    @staticmethod
    def is_symmetric(root: Optional[TreeNode]) -> bool:
        symmetric = True
        list_of_round = [root.left, root.right]
        list_value = []
        list_next_round = []
        while symmetric:
            for node in list_of_round:
                list_value.append(node.val)
                list_next_round.append(node.left)
                list_next_round.append(node.right)
            if list_value == list_value[::-1] and len(list_value) % 2 == 0:
                if len([i for i in list_next_round if i is not None]) > 0:
                    list_of_round = list_next_round
                    list_value = []
                    list_next_round = []
                else:
                    return True
            else:
                symmetric = False
        return False


if __name__ == '__main__':
    print(Solution.is_symmetric(root_))




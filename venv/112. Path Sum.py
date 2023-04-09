"""Given the root of a binary tree and an integer targetSum, return true if the
tree has a root-to-leaf path such that adding up all the values along the path
equals targetSum. A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
        output_list: list = []
        if isinstance(root, TreeNode):
            items: list[tuple] = [(root, root.val)]
            while items:
                item: tuple = items.pop()
                node: TreeNode = item[0]
                if node.left or node.right:
                    if node.left:
                        items.append((node.left, item[1] + node.left.val))
                    if node.right:
                        items.append((node.right, item[1] + node.right.val))
                else:
                    output_list.append(item[1])
        return target_sum in output_list


node_1_5 = TreeNode(7)
node_1_4 = TreeNode(15)
node_1_3 = TreeNode(20, node_1_4, node_1_5)
node_1_2 = TreeNode(9)
root_1 = TreeNode(3, node_1_2, node_1_3)

node_2_7 = TreeNode(4)
node_2_6 = TreeNode(4)
node_2_5 = TreeNode(3)
node_2_4 = TreeNode(3, node_2_6, node_2_7)
node_2_3 = TreeNode(2)
node_2_2 = TreeNode(2, node_2_4, node_2_5)
root_2 = TreeNode(1, node_2_2, node_2_3)

root_3 = TreeNode(12)


assert Solution.has_path_sum(root_1, 12)
assert Solution.has_path_sum(root_1, 30)
assert Solution.has_path_sum(root_1, 38)
assert Solution.has_path_sum(root_2, 3)
assert Solution.has_path_sum(root_2, 6)
assert Solution.has_path_sum(root_2, 10)
assert Solution.has_path_sum(root_3, 12)
assert not Solution.has_path_sum(root_3, 10)
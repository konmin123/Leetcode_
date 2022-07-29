"""A binary tree's maximum depth is the number of nodes along the
longest path from the root node down to the farthest leaf node.



Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


class Solution:
    @staticmethod
    def max_depth(root_: Optional[TreeNode]) -> int:
        """Итеративный способ обхода в ширину для поиска глубины"""
        if isinstance(root_, TreeNode):
            queue = [root_]
            queue_next_tour = []
            depth = 0
            while queue:
                for node in queue:
                    if node.left:
                        queue_next_tour.append(node.left)
                    if node.right:
                        queue_next_tour.append(node.right)
                depth += 1
                queue = queue_next_tour
                queue_next_tour = []
                print(queue)
            return depth
        else:
            return 0

    @staticmethod
    def max_depth_rec(root_: Optional[TreeNode]) -> int:
        """Рекурсивный способ поиска глубины"""
        def dfs(root__, depth):
            if not root__:
                return depth
            return max(dfs(root__.left, depth + 1), dfs(root__.right, depth + 1))

        return dfs(root, 0)


if __name__ == '__main__':
    print(Solution.max_depth_rec(root))

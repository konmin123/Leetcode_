"""Скрипт для создания деревьев"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeCreator:
    @staticmethod
    def tree_creator(sequence):
        root = TreeNode(sequence[0])
        nodes_for_links = [root]
        list_new_nodes = []
        current_index = 1
        while current_index < len(sequence):
            for i in range(2 * len(nodes_for_links)):
                value_for_new_node = sequence[current_index]
                if value_for_new_node:
                    list_new_nodes.append(TreeNode(value_for_new_node))
                else:
                    list_new_nodes.append(None)
                current_index += 1
            count_for_link = 0
            for node in nodes_for_links:
                if node is not None:
                    node.left = list_new_nodes[count_for_link]
                    count_for_link += 1
                    node.right = list_new_nodes[count_for_link]
                    count_for_link += 1
                else:
                    count_for_link += 2
            nodes_for_links = list_new_nodes
            list_new_nodes = []
        return root

    @staticmethod
    def list_values_tree(root: TreeNode):
        current_level = [root]
        next_level = []
        list_values = []
        flag = True
        while flag:
            flag = False
            for node in current_level:
                if node is not None:
                    list_values.append(node.val)
                    next_level.append(node.left)
                    next_level.append(node.right)
                    flag = True
                else:
                    list_values.append(None)
                    next_level.append(None)
                    next_level.append(None)
            current_level = next_level
            next_level = []
        return list_values


if __name__ == '__main__':
    s = TreeCreator.tree_creator([10, None, 15, None, None, 13, None])
    print(TreeCreator.list_values_tree(s))


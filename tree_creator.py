"""Скрипт для создания деревьев"""


class TreeNode:
    """Конструктор ноды дерева"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self, data: list = None):
        """Конструктор дерева"""
        self.root = TreeNode()

        if data is not None:
            self.root.val = data[0]
            nodes_for_link = [self.root]
            list_new_nodes = []
            current_index = 1
            while current_index < len(data):
                for i in range(2 * len(nodes_for_link)):
                    value_for_new_node = data[current_index]
                    if value_for_new_node is not None:
                        list_new_nodes.append(TreeNode(value_for_new_node))
                    else:
                        list_new_nodes.append(None)
                    current_index += 1
                index_for_link = 0
                for node in nodes_for_link:
                    if node is not None:
                        node.left = list_new_nodes[index_for_link]
                        index_for_link += 1
                        node.right = list_new_nodes[index_for_link]
                        index_for_link += 1
                    else:
                        index_for_link += 2
                nodes_for_link = list_new_nodes
                list_new_nodes = []

    def list_values_tree(self):
        """Метод получения списка значений нод дерева"""
        current_level = [self.root]
        next_level = []
        list_values = []
        while True:
            for node in current_level:
                if node is not None:
                    list_values.append(node.val)
                    next_level.append(node.left)
                    next_level.append(node.right)
                else:
                    list_values.append(None)
                    next_level.append(None)
                    next_level.append(None)
            if not all(x is None for x in next_level):
                current_level = next_level
                next_level = []
            else:
                break
        return list_values


if __name__ == '__main__':
    s = Tree([10, None, 15, None, None, 13, None])
    print(Tree.list_values_tree(s))

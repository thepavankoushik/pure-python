def lca(node, n1, n2):
    if node is None:
        return 0
    if n1 >= node.data and n2 >= node.data:
        lca(node.right, n1, n2)
    if n1 <= node.data and n2 <= node.data:
        lca(node.left, n1, n2)
    return node.data


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


def insert(node, data):
    if node is None:
        return Node(data)
    else:
        if data <= node.data:
            node.left = insert(node.left, data)
        else:
            node.right = insert(node.right, data)
        return node


if __name__ == "__main__":
    root = None
    root = insert(root, 4)
    insert(root, 2)
    insert(root, 1)
    insert(root, 3)
    insert(root, 6)
    insert(root, 5)
    print(lca(root, 2, 1))

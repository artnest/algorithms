class TreeNode:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def get_root(self):
        return self.root

    def put(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            parent = None
            node = self.root
            while node is not None:
                parent = node
                if key < node.key:
                    node = node.left
                elif key > node.key:
                    node = node.right
                else:
                    return

            if key < parent.key:
                parent.left = TreeNode(key)
            elif key > parent.key:
                parent.right = TreeNode(key)

    def preorder(self, node):
        if node:
            print(node.key)
            self.preorder(node.left)
            self.preorder(node.right)

    def preorder_file(self, node, file):
        if node:
            file.write(str(node.key) + "\n")
            self.preorder_file(node.left, file)
            self.preorder_file(node.right, file)


if __name__ == '__main__':
    bst = BinarySearchTree()
    with open("input.txt", "r") as fin:
        for key in fin.readlines():
            bst.put(int(key))

    with open("output.txt", "w") as fout:
        bst.preorder_file(bst.get_root(), fout)

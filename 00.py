class TreeNode:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root
        self.keys_sum = 0

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
        self.keys_sum = self.keys_sum + key

if __name__ == '__main__':
    bst = BinarySearchTree()
    with open("input.txt", "r") as fin:
        for key in fin.readlines():
            bst.put(int(key))

    with open("output.txt", "w") as fout:
        fout.write(str(bst.keys_sum))

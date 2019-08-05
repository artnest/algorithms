class TreeNode:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.l_height = -1
        self.r_height = -1
        self.l_size = 0
        self.r_size = 0

    def __iter__(self):
        if self:
            if self.left:
                for node in self.left:
                    yield node
            yield self
            if self.right:
                for node in self.right:
                    yield node

    def _count_subtrees_(self):
        if self.left:
            self.l_size = len([i for i in self.left])
        if self.right:
            self.r_size = len([i for i in self.right])


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def __iter__(self):
        return self.root.__iter__()

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

    def minimum(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def remove(self, key):
        self.root = self._remove_(self.root, key)

    def _remove_(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._remove_(root.left, key)
        elif key > root.key:
            root.right = self._remove_(root.right, key)
        elif root.left and root.right:
            root.key = self.minimum(root.right).key
            root.right = self._remove_(root.right, root.key)
        elif root.left:
            root = root.left
        else:
            root = root.right
        return root

    def _height_(self, node):
        if not node:
            return 0
        if node.left:
            l_h = self._height_(node.left)
        else:
            l_h = -1
        if node.right:
            r_h = self._height_(node.right)
        else:
            r_h = -1
        return max(l_h, r_h) + 1

    def update_info(self):
        for node in self:
            node.l_height = self._height_(node.left)
            node.r_height = self._height_(node.right)
        for node in self:
            node._count_subtrees_()

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
    with open("in.txt", "r") as fin:
        for key in fin.readlines():
            bst.put(int(key))
    bst.update_info()

    special_keys = []
    for node in bst:
        if node.left and node.right:
            if node.l_height == node.r_height and node.l_size != node.r_size:
                special_keys.append(node.key)

    if len(special_keys) % 2 != 0:
        special_keys.sort()
        key_to_remove = special_keys[len(special_keys) // 2]
        bst.remove(key_to_remove)

    with open("out.txt", "w") as fout:
        bst.preorder_file(bst.get_root(), fout)

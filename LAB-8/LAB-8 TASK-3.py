import random
class BST:
    class BTNode:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def add(self, d, t):
        if not t:
            return self.BTNode(d)
        if t.data > d:
            t.left = self.add(d, t.left)
        elif t.data < d:
            t.right = self.add(d, t.right)
        return t

    def add_node(self, d):
        self.root = self.add(d, self.root)

    def inorder(self, t):
        if t:
            self.inorder(t.left)
            print(t.data, end=' ')
            self.inorder(t.right)

    def inorder_traversal(self):
        self.inorder(self.root)
        print()

    def preorder(self, t):
        if t:
            print(t.data, end=' ')
            self.preorder(t.left)
            self.preorder(t.right)

    def preorder_traversal(self):
        self.preorder(self.root)
        print()

    def count_nodes(self, t):
        if not t: return 0
        return self.count_nodes(t.left) + self.count_nodes(t.right) + 1

    def inorder_array(self, t, array, index):
        if t:
            index = self.inorder_array(t.left, array, index)
            array[index] = t.data
            index = self.inorder_array(t.right, array, index + 1)
        return index

    def add_binary_search(self, array, start, end):
        if start <= end:
            mid = (start + end) // 2
            self.add_node(array[mid])
            self.add_binary_search(array, start, mid - 1)
            self.add_binary_search(array, mid + 1, end)

    def check_and_balance_tree(self, count_nodes):
        array = [None] * (count_nodes + 1)
        self.inorder_array(self.root, array, 1)
        self.remove_nodes(self.root)
        self.root = None
        self.add_binary_search(array, 1, count_nodes)

    def check_and_balance(self):
        left = self.count_nodes(self.root.left)
        right = self.count_nodes(self.root.right)
        if abs(left - right) > 1:
            self.check_and_balance_tree(left + right + 1)

    def remove_nodes(self, t):
        if t:
            self.remove_nodes(t.left)
            self.remove_nodes(t.right)
            del t

    def __del__(self):
        self.remove_nodes(self.root)

if __name__ == "__main__":
    tree = BST()
    for _ in range(20):
        tree.add_node(random.randint(100, 999))
    tree.preorder_traversal()
    tree.inorder_traversal()
    tree.check_and_balance()
    tree.preorder_traversal()
    tree.inorder_traversal()
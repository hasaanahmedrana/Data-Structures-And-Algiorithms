import random
import math
print('----------------TASK-1-------------')
class Node:
    def __init__(self, value: int or str):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVL:
    def __init__(self):
        self.root = None

    def __str__(self) -> str:
        return str(self.root.value)

    def height(self, node: Node) -> int:
        if node is None:
            return 0
        return node.height

    def insert(self, root: Node, value: int or str) -> Node:
        if not root:
            return Node(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        elif value > root.value:
            root.right = self.insert(root.right, value)
        else:
            return root
        root.height = self.calculateHeight(root)
        return self.rotation(root)

    def insert_value(self, value: int):
        self.root = self.insert(self.root, value)

    def balance_factor(self, node):
        if node is None: return 0
        return self.height(node.left) - self.height(node.right)

    def rotation(self, node: Node) -> Node:
        bal_f = self.balance_factor(node)
        if bal_f > 1:
            left_bal_f = self.balance_factor(node.left)
            return self.rotation_ll(node) if left_bal_f > 0 else self.rotation_lr(node)

        elif bal_f < -1:
            right_bal_f = self.balance_factor(node.right)
            return self.rotation_rr(node) if right_bal_f < 0 else  self.rotation_rl(node)
        return node

    def rotation_ll(self, node: Node) -> Node:
        new_root = node.left
        child_of_old = new_root.right
        new_root.right = node
        node.left = child_of_old
        node.height = self.calculateHeight(node)
        new_root.height = self.calculateHeight(new_root)
        return new_root

    def rotation_rr(self, node: Node) -> Node:
        new_root = node.right
        child_of_old = new_root.left
        new_root.left = node
        node.right = child_of_old
        node.height = self.calculateHeight(node)
        new_root.height = self.calculateHeight(new_root)
        return new_root

    def rotation_lr(self, node: Node) -> Node:
        node.left = self.rotation_rr(node.left)
        return self.rotation_ll(node)

    def rotation_rl(self, node: Node) -> Node:
        node.right = self.rotation_ll(node.right)
        return self.rotation_rr(node)

    def inorder(self, p):
        if p.left:
            self.inorder(p.left)
        print(p.value, end=" ")
        if p.right:
            self.inorder(p.right)

    def inorder_traversal(self):
        if self.root:
            self.inorder(self.root)

    def getHeight(self) -> int:
        return self.calculateHeight(self.root)

    def calculateHeight(self, root: Node) -> int:
        if root is None:
            return 0
        lh = self.calculateHeight(root.left)
        rh = self.calculateHeight(root.right)
        return max(lh, rh) + 1


if __name__ == '__main__':
    tree = AVL()
    print(round(math.log2(500)))
    for _ in range(500):
        val = random.randint(10, 2000)
        tree.insert_value(val)
    print("Height:", tree.getHeight())
    print("\nIn Order: ", end="")
    tree.inorder_traversal()

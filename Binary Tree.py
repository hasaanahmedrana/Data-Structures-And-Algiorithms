'''Binary Tree: A tree in which each node has at most two children.
- Strict/Proper/Full Binary Tree: A binary tree in which each node has either 0 or 2 children
            .or
            We can say each node have 2 children except leaves.
Complete Binary Tree: A binary tree in which all levels are completely filled except possibly the last level and the last level has all keys as left as possible.
Perfect Binary Tree: A binary tree in which all internal nodes have two children and all leaf nodes are at the same level.
        Each Perfect binary tree is Strict and Complete binary tree.
Perfect tree have "2^(no. of levels) -1" or "2^(height+1)-1"  number of nodes.
Degenerate Binary tree: Each internal node have only one child. Left and right skewed tree are examples of degenerate binary trees.

Empty Tree: Tree with no node.
--> Height of tree with one node is zero, while height of empty tree is -1.
--> Maximum number of nodes at any level i is 2^i
--> Maximum number of nodes in a binary tree with height h is "2^(h+1) - 1"
--> Minimum number of nodes in a binary tree with height h is "h + 1"
'''

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self):
        self.root = None



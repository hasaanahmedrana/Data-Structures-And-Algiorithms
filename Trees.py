'''Tree: A data Structure (non-linear) to store data in hierarchical manner. It is a recursive data structure.
Tree Terminologies:
-> A tree is made up of nodes and edges. The topmost node is called the root of the tree.
-> The nodes that are directly under the root node are called the children of the root node.
-> The nodes that are directly above the child nodes are called the parent nodes.
-> The nodes that do not have any children are "leaf nodes".
-> The nodes with same parents are  siblings.
-> The nodes that are connected by edges (direct linkage) are called adjacent nodes.
DEPTH OF A NODE: The number of edges from the root node to that  node.
HEIGHT OF A NODE: The number of edges from the node to the deepest leaf node(most away leaf child)
HEIGHT OF A TREE: The height of the root node.
LEVEL OF A NODE: Nodes with the same depth are on the same level.
DEGREE OF A NODE: number of child nodes of that node
DEGREE OF A TREE: maximum degree in the tree is tree's degree.

Conditions for a tree:
1- Every node has a single Parent Node.
2- There is only one path between any two nodes in the tree.
3- There's no cycle in the tree.
4- For n nodes, there are n-1 edges(connections).


 Types of Trees:
 1. Binary Tree: A tree in which each node has at most two children.
 2. Binary Search Tree: A binary tree in which the left child of a node has a value less than the parent node and the right child has a value greater than the parent node.
 3. AVL Tree: A binary search tree in which the height of the left and right subtrees of each node differs by at most one.
 4. Red-Black Tree: A binary search tree in which each node is colored either red or black and the following properties are satisfied:
    a. The root node is black.
    b. The children of a red node are black.
    c. Every path from a node to a leaf node has the same number of black nodes.
5. B-Tree: A tree in which each node can have more than two children.
6. Trie: A tree in which each node represents a character and the path from the root node to a leaf node represents a word.
7. Segment Tree: A tree in which each node represents a range of values and the path from the root node to a leaf node represents a segment of the range.

ADVANTAGES OF TREE:
1. Trees are used to represent hierarchical data.
2. Trees provide an efficient way to search, insert, and delete elements e.g binary search tree.
3. Trees are used in computer science to represent file systems, parse trees, and game trees.'''



from collections import deque
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

class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return f'{self.data}'


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data:int):
        new = Node(data)
        if not self.root:
            self.root = new
        temp = self.root
        while temp:
            if data > temp.data:
                if temp.right == None:
                    temp.right = new
                    new.parent = temp
                    return
                temp = temp.right
            elif data < temp.data:
                if temp.left == None:
                    temp.left = new
                    new.parent = temp
                    return
                temp = temp.left
            else:
                return

    def search(self, data: int) -> bool:
        ''''''
        temp = self.root
        while temp:
            if data == temp.data:
                return True
            elif data > temp.data:
                temp = temp.right
            elif data < temp.data:
                temp = temp.left
        return False

    def successor(self, key: int) -> int or None:
        '''Successor of a node:
        1- if right child of node is not None, then successor is the leftmost node in the right subtree.
        2- if left child of node is not None, then successor is the first ancestor of node whose left child is also ancestor of node.'''
        temp = self.root
        while temp:
            if key == temp.data:
                break
            elif key > temp.data:
                temp = temp.right
            elif key < temp.data:
                temp = temp.left
        print('key found:',temp.data)
        if temp.right:
            print('Right child of key:',temp.right.data)
            temp = temp.right
            while temp.left:
                temp = temp.left
            return temp.data
        parent = temp.parent
        while parent and temp == parent.right:
            temp = parent
            parent = parent.parent
        return parent.data if parent else None


    def predecessor(self, key: int) -> int or None:
        '''Predecessor of a node:
        1- if left child of node is not None, then predecessor is the rightmost node in the left subtree.
        2- if left child of node is None, then predecessor is the first ancestor of node whose right child is also ancestor of node.'''
        if not self.root: return None
        temp = self.root
        flag = False
        while temp:
            if temp.data == key:
                flag = True
                break
            elif key > temp.data:
                temp = temp.right
            elif key < temp.data:
                temp = temp.left
        if not flag: return None
        if temp.left:
            temp = temp.left
            while temp.right:
                temp = temp.right
            return temp.data
        parent = temp.parent
        while parent and temp == parent.left:
            temp = parent
            parent = parent.parent
        return parent.data if parent else None

    def search_and_return(self, data):
        temp = self.root
        while temp:
            if data == temp.data:
                return temp
            elif data > temp.data:
                temp = temp.right
            elif data < temp.data:
                temp = temp.left
        return False


    def delete(self, data):
        if not self.root: return 'Tree is empty.'
        elif not self.search(data): return 'Node not found.'
        temp = self.search_and_return(data)
        if not temp.left and not temp.right:
            if temp == temp.parent.left:
                temp.parent.left = None
            else:
                temp.parent.right = None
            del temp
            return 'Node deleted successfully'
        elif temp.left and not temp.right:
            if temp == temp.parent.left:
                temp.parent.left = temp.left
            else:
                temp.parent.right = temp.left
            temp.left.parent = temp.parent
            del temp
            return 'Node deleted successfully'
        elif not temp.left and temp.right:
            if temp == temp.parent.left:
                temp.parent.left = temp.right
            else:
                temp.parent.right = temp.right
            temp.right.parent = temp.parent
            del temp
            return 'Node deleted successfully'
        else:
            successor = temp.right
            while successor.left:
                successor = successor.left
            temp.data = successor.data

            if successor == successor.parent.right:
                successor.parent.right = successor.right
            else:
                successor.parent.left = successor.right
            if successor.right:
                successor.right.parent = successor.parent
            del successor
            return 'Node deleted successfully'

    def _count(self, node,count):
        if node is None: return count
        return  self._count(node.left, count) + self._count(node.right,count) + 1

    def total_elements(self):
        return f'{self._count(self.root, 0) if self.root else 0}'




    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.data, end=' ')
            self._inorder(node.right)

    def _preorder(self, node):
        if node:
            print(node.data, end=' ')
            self._preorder(node.left)
            self._preorder(node.right)

    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.data, end=' ')

    def display_in_order(self):
        print('In Order:', end=' ')
        if not self.root: return None
        self._inorder(self.root)
        print()

    def display_pre_order(self):
        print('Pre Order:', end=' ')
        if not self.root: return None
        self._preorder(self.root)
        print()

    def display_post_order(self):
        print('Post Order:', end=' ')
        if not self.root: return None
        self._postorder(self.root)
        print()
    
    def display_level_order(self):
        print()
        root = self.root
        if not root: return
        q = deque([(root,1)])
        self._levelorder(q)
        print()

    def _levelorder(self,q):
        if not q: return;
        node, level = q.popleft()
        print(f'Node: {node.data}, Level: {level}')
        if node.left:
            q.append((node.left, level+1))
        if node.right:
            q.append((node.right, level+1))
        self._levelorder(q)


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(20)
    bst.insert(30)
    bst.insert(25)
    bst.insert(23)
    bst.insert(24)
    bst.insert(27)
    bst.insert(0)
    bst.insert(5)
    bst.insert(3)
    bst.insert(4)
    bst.insert(2)
    bst.insert(-1)
    bst.insert(13)
    bst.insert(100)
    print(bst.predecessor(13))
    print(bst.successor(13))
    print('Pre-order Sequence:',end=' ')
    bst.display_pre_order()
    print('In-order Sequence:',end=' ')
    bst.display_in_order()
    print('Post-order Sequence:',end=' ')
    bst.display_post_order()
    print('Level-order Sequence:',end=' ')
    bst.display_level_order()
    print('Total Elements Number:', bst.total_elements())
    print(bst.delete(-1)) #Deleting leaf node
    bst.display_in_order() #verify deletion by checking in order sequence
    print(bst.delete(23)) #Deleting node with one child
    bst.display_in_order()
    print(bst.delete(20)) #Deleting node with two children.
    bst.display_in_order()
    
    # t = BinaryTree()
    # t.insert(10)
    # t.insert(5)
    # t.insert(15)
    # t.insert(3)
    # t.insert(7)
    # t.insert(13)
    # t.insert(20)
    # t.insert(2)
    # t.insert(4)
    # t.insert(6)
    # print(t.search(17))
    # print(t.search(20))
    # print(t.search(7))
    # print(t.search(33))
    # print(t.successor(20))
    # print(t.predecessor(20))
    # t.display_in_order()
    # t.display_pre_order()
    # t.display_post_order()
    # print(t.delete(12))
    # print(t.delete(13))
    # t.display_in_order()
    # t.display_pre_order()
    # t.display_post_order()
    # print(t.delete(5))
    # t.display_in_order()
    # t.display_pre_order()
    # t.display_post_order()



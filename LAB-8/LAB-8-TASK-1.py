'''
All 17 functions are implemented in this file of task-1.
A representative picture of the tree I created in the task is attached with it,
It can help to verify proper working of each function.
'''

class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def set_value(self, value):
        self.value = value
    def set_left(self, left):
        self.left = left
    def set_right(self, right):
        self.right = right
    def get_value(self):
        return self.value
    def get_left(self):
        return self.left
    def get_right(self):
        return self.right
    def __str__(self):
        return f'{self.value}'


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_element_root(self, element):
        if not self.root:
            self.root = element
        else:
            raise Exception('Root already Exists.')

    def search(self, root, elem):
        if root is None: return None
        if root == elem: return root
        left_subtree  = self.search(root.left, elem)
        if left_subtree is not None: return left_subtree
        right_subtree  = self.search(root.right, elem)
        if right_subtree is not None: return right_subtree
        return None


    def insert_left_child(self, parent, child):
        finding_parent = self.search(self.root, parent)
        if not finding_parent: return
        if finding_parent.left: return
        finding_parent.left = child


    def insert_right_child(self, parent, child):
        finding_parent =  self.search(self.root, parent)
        if not finding_parent: return
        if finding_parent.right: return
        finding_parent.right = child

    def display_pre_order(self, node):
        if node:
            print(node.value, end=' ')
            self.display_pre_order(node.left)
            self.display_pre_order(node.right)


    def display_in_order(self, node):
        if node:
            self.display_in_order(node.left)
            print(node.value, end=' ')
            self.display_in_order(node.right)

    def display_post_order(self, node):
        if node:
            self.display_post_order(node.left)
            self.display_post_order(node.right)
            print(node.value, end=' ')
    def non_rec_pre_order(self):
        if not self.root: return None
        lst = []
        lst.append(self.root)
        while lst != []:
            node = lst.pop()
            print(node.value, end=' ')
            if node.right:
                lst.append(node.right)
            if node.left:
                lst.append(node.left)

    def non_rec_in_order(self):
        if not self.root: return None
        lst = []
        temp = self.root
        while True:
            while temp is not None:
                lst.append(temp)
                temp = temp.left
            if len(lst) == 0:
                break
            temp = lst.pop()
            print(temp.value, end=' ')
            temp = temp.right
    def non_rec_post_order(self):
        if not self.root:
            print('Tree is empty at the moment.')
            return
        lst1 = []; lst2 = []
        lst1.append(self.root)
        while lst1:
            node = lst1.pop()
            lst2.append(node)
            if node.left: lst1.append(node.left);
            if node.right: lst1.append(node.right)
        while lst2:
            print(lst2.pop(),end= ' ')



    def _count(self, node,count):
        if node is None: return count
        return  self._count(node.left, count) + self._count(node.right,count) + 1

    def count_nodes(self):
        return f'Count of nodes is : {self._count(self.root, 0) if self.root else 0}'

    def leaf(self, node):
        if node is None: return 0
        if node.left is None and node.right is None: return 1
        return self.leaf(node.left) + self.leaf(node.right)

    def count_leaf_nodes(self):
        return f'Count of leaf nodes is :{self.leaf(self.root)}'

    def _minimum(self, root, mini):
        if root is None: return mini
        if root.value < mini:
            mini = root.value
        mini = min(self._minimum(root.left, mini), self._minimum(root.right, mini))
        return mini

    def min_value(self):
        return f'Minimum valued node is:{self._minimum(self.root, self.root.value) if self.root else None}'

    def descendants(self, root):
        descendants = []
        if root:
            if root.left:
                descendants.append(root.left.value)
                descendants += self.descendants(root.left)
            if root.right:
                descendants.append(root.right.value)
                descendants += self.descendants(root.right)
        return descendants

    def display_descendants(self, node_value):
        element = self.search(self.root, node_value)
        if not element: return 'Element not found'
        return f'Descendants of {element.value} are: {self.descendants(element)}'

    def _height(self, node, height):
        if node is None: return height
        height +=1
        return max(self._height(node.left, height),self._height(node.right,height))

    def height(self):
        return self._height(self.root, 0) - 1

    def ancestors(self, node, val, parent=None):
        if parent is None:
            parent = {}
        if not node:
            return None
        if node.value == val:
            ancestors = []
            while node:
                node = parent.get(node)
                if node:
                    ancestors.append(node.value)
            return ancestors
        if node.left:
            parent[node.left] = node
        if node.right:
            parent[node.right] = node
        left = self.ancestors(node.left, val, parent)
        if left is not None:
            return left
        return self.ancestors(node.right, val, parent)

    def display_ancestors(self, node_value):
        ancestor = self.ancestors(self.root,node_value)
        return f'Ancestors of {node_value} are: {ancestor}'

    def node_height(self,node):
        return self._height(node, 0) - 1

    def find_balance_factor(self):
        return self.node_height(self.root.left) - self.node_height(self.root.right)

    def delete_element(self, element):
        element = self.search(element)
        element = None



if __name__ == '__main__':
    tree = BinaryTree()
    root = BTNode(20)
    tree.insert_element_root(root)
    root_left = BTNode(15)
    root_right = BTNode(10)
    tree.insert_left_child(root, root_left)
    tree.insert_right_child(root, root_right)
    five = BTNode(5);six = BTNode(6);seven = BTNode(7);nine = BTNode(9)
    tree.insert_left_child(root_left, BTNode(12))
    tree.insert_right_child(root_left, BTNode(17))
    tree.insert_left_child(root_right, five)
    tree.insert_left_child(five, six)
    tree.insert_left_child(six, seven)
    tree.insert_right_child(root_right, nine)
    print(tree.count_nodes())
    print(tree.count_leaf_nodes())
    print(tree.min_value())
    print(tree.display_descendants(root))
    print(tree.display_descendants(root_left))
    print(tree.display_descendants(root_right))
    print(tree.display_ancestors(10))
    print(tree.display_ancestors(6))
    print(f'Pre-order  Recursive:  ', end='')
    tree.display_pre_order(root)
    print()
    print(f'Pre-order Non-recursive: ', end='')
    tree.non_rec_pre_order()
    print()
    print(f'In-order  Recursive:  ', end='')
    tree.display_in_order(root)
    print()
    print(f'In-order Non-recursive: ', end='')
    tree.non_rec_in_order()
    print()
    print(f'Post-order  Recursive:  ', end='')
    tree.display_post_order(root)
    print()
    print(f'Post-order Non-recursive: ', end='')
    tree.non_rec_post_order()
    print()
    print('Height of the tree is:', tree.height())
    print('Balance factor of the tree is:', tree.find_balance_factor())









'''This file contains all 6 functions of task-2.
The image od tree of sample run is attached with it.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
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


class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert_element(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return
        temp = self.root
        while True:
            if value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    new_node.parent = temp
                    return
                else:
                    temp = temp.right
            elif value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    new_node.parent = temp
                    return
                else:
                    temp = temp.left
            else:
                return

    def search(self, value: int):
        temp = self.root
        while temp:
            if value == temp.value:
                return temp
            elif value > temp.value:
                temp = temp.right
            elif value < temp.value:
                temp = temp.left
        return False



    def delete_element(self, value):
        if not self.root: return None
        element = self.search(value)
        if not element: return None
        if element.left is None and element.right is None:
            if element == element.parent.left:
                element.parent.left = None
            else:
                element.parent.right = None
        elif element.left is not None and element.right is not None:
            temp = element.right
            while temp.left:
                temp = temp.left

            # temp is successor of element
            element.value = temp.value
            if temp == temp.parent.left:
                temp.parent.left = temp.right
            else:
                temp.parent.right = temp.right
            if temp.right:
                temp.right.parent = temp.parent
        else:
            if element.left:
                child = element.left
            else:
                child = element.right
            if element == element.parent.left
                element.parent.left = child
            else:
                element.parent.right = child
            child.parent = element.parent


    def pre_order_helper(self, node):
        if node:
            print(node.value, end=' ')
            self.pre_order_helper(node.left)
            self.pre_order_helper(node.right)
    def display_pre_order(self):
        if not self.root: return None
        self.pre_order_helper(self.root)



    def in_order_helper(self, node):
        if node:
            self.in_order_helper(node.left)
            print(node.value, end=' ')
            self.in_order_helper(node.right)
    def display_in_order(self):
        if not self.root: return None
        self.in_order_helper(self.root)


    def post_order_helper(self, node):
        if node:
            self.post_order_helper(node.left)
            self.post_order_helper(node.right)
            print(node.value, end=' ')
    def display_post_order(self):
        if not self.root: return None
        self.post_order_helper(self.root)

    def _count(self, node,count):
        if node is None: return count
        return  self._count(node.left, count) + self._count(node.right,count) + 1

    def total_elements(self):
        return f'{self._count(self.root, 0) if self.root else 0}'

if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert_element(10)
    bst.insert_element(20)
    bst.insert_element(30)
    bst.insert_element(25)
    bst.insert_element(23)
    bst.insert_element(24)
    bst.insert_element(27)
    bst.insert_element(0)
    bst.insert_element(5)
    bst.insert_element(3)
    bst.insert_element(4)
    bst.insert_element(2)
    bst.insert_element(-1)
    bst.insert_element(13)
    bst.insert_element(100)
    print('Pre-order Sequence:',end=' ')
    bst.display_pre_order()
    print()
    print('In-order Sequence:',end=' ')
    bst.display_in_order()
    print()
    print('Post-order Sequence:',end=' ')
    bst.display_post_order()
    print()
    print('Total Elements Number:', bst.total_elements())
    bst.delete_element(-1) #Deleting leaf node
    bst.display_in_order() #verify deletion by checking in order sequence
    print()
    bst.delete_element(23) #Deleting node with one child
    bst.display_in_order()
    print()
    bst.delete_element(20) #Deleting node with two children.
    bst.display_in_order()
    print()
    print('-'*40)


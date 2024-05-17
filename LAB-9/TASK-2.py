print('-------------TASK-2--------------')
class BSTNode:
    def __init__(self, value: int or str):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_helper(self, node, value):
        new_one = BSTNode(value)
        if value < node.value:
            if node.left:
                self.insert_helper(node.left, value)
            else:
                node.left = new_one
        elif value > node.value:
            if node.right:
                self.insert_helper(node.right, value)
            else:
                node.right = new_one
        else:
            return

    def insert(self, value):
        if not self.root:
            self.root = BSTNode(value)
        else:
            self.insert_helper(self.root, value)

    def pre_order_helper(self, node):
        if not node:
            return
        print(node.value, end=' ')
        self.pre_order_helper(node.left)
        self.pre_order_helper(node.right)

    def display_pre_order(self):
        self.pre_order_helper(self.root)
        print()

    def in_order_helper(self, node):
        if not node:
            return
        self.in_order_helper(node.left)
        print(node.value, end=' ')
        self.in_order_helper(node.right)

    def display_in_order(self):
        self.in_order_helper(self.root)
        print()

    def post_order_helper(self, node):
        if not node:
            return
        self.post_order_helper(node.left)
        self.post_order_helper(node.right)
        print(node.value, end=' ')

    def display_post_order(self):
        self.post_order_helper(self.root)
        print()

    # def find_children(self, in_order, pre_order,final):
    #     indexes = {}
    #     for each in in_order:
    #         indexes[each] = pre_order.index(each)
    #     indexes = dict(sorted(indexes.items(), key=lambda item: item[1]))
    #     for i, j in indexes.items():
    #         final.append(i)


    # def construct_from_traversals(self, in_order, pre_order):
    #     final = []
    #     root = pre_order[0]
    #     idx = in_order.index(root)
    #     final.append(root)
    #     left = in_order[:idx] ; right = in_order[idx+1:]
    #     self.find_children(left, pre_order, final)
    #     self.find_children(right, pre_order, final)
    #     for each in final:
    #         self.insert(each)
    #     return self.root

    def construct_from_traversals(self, in_order, pre_order):
        if in_order == []:
            return None

        elif pre_order == []:
            return None
        root = pre_order.pop(0)
        parent_element = BSTNode(root)
        idx = in_order.index(parent_element.value)
        parent_element.left = self.construct_from_traversals(in_order[:idx], pre_order)
        parent_element.right = self.construct_from_traversals(in_order[idx+1:], pre_order)
        return parent_element



if __name__ == '__main__':

    bst = BinarySearchTree()
    in_order = ['D', 'B', 'E', 'A', 'F', 'C']
    pre_order = ['A', 'B', 'D', 'E', 'C', 'F']

    bst.root = bst.construct_from_traversals(in_order, pre_order)

    # Verify constructed tree
    print("In-order traversal of constructed BST:")
    bst.display_in_order()

    # Verify constructed tree
    print("Post-order traversal of constructed BST:")
    bst.display_post_order()


    # Example 2 usage:
    bst2 = BinarySearchTree()
    in_order = [5, 10, 15, 25, 27, 30, 35, 40, 45, 50, 52, 55, 60, 65, 70,
                75, 80, 85, 90, 100]
    pre_order = [50, 25, 10, 5, 15, 40, 30, 27, 35, 45, 75, 60, 55, 52, 65,
                 70, 90, 80, 85, 100]

    bst2.root = bst2.construct_from_traversals(in_order, pre_order)

    # Verify constructed tree
    print("In-order traversal of constructed BST:")
    bst2.display_in_order()

    # Verify constructed tree
    print("Post-order traversal of constructed BST:")
    bst2.display_post_order()
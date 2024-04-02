# class Node:
#     '''
#    Node class for linked list
#   Every node has data and next (a pointer to the next node)
#     '''
#
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:

#
#     def __init__(self):
#         self.head = Node()
#
#     def is_empty(self):
#         return self.head.next == None
#     def append(self,data):
#         new_node = Node(data)
#         cur = self.head
#         while cur.next != None:
#             cur = cur.next
#         cur.next = new_node
#     def length(self):
#         cur = self.head
#         length = 0
#         while cur.next != None:
#             length += 1
#             cur = cur.next
#         return length
#
#     def display(self):
#         elems = []
#         cur_node = self.head
#         if cur_node.next == None:
#             print('List is empty')
#             return
#         while cur_node.next != None:
#             cur_node = cur_node.next
#             elems.append(cur_node.data)
#         print(elems)
#
#     def get(self, idx):
#         if idx >= self.length():
#             print('Index out of range')
#             return
#         cur_node = self.head
#         cur_idx = 0
#         while cur_idx != idx:
#             cur_node = cur_node.next
#             cur_idx += 1
#         return cur_node.data
#
#     def erase(self, idx):
#         if idx >= self.length():
#             print('Index out of range')
#             return
#         cur_node = self.head
#         cur_idx = 0
#         while True:
#             last_node = cur_node
#             cur_node = cur_node.next
#             if cur_idx == idx:
#                 last_node.next = cur_node.next
#                 return
#             cur_idx += 1
# my_list = LinkedList()
# my_list.display()
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# my_list.append(4)
# my_list.display()
# print(my_list.get(2))
# my_list.erase(2)
# my_list.display()
# your_list = LinkedList()
# your_list.display()
# print(your_list.is_empty())
# print(my_list.is_empty())

class Node:
    '''
    Node class for linked list
   Every node has data and next (a pointer to the next node)
    '''
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Linkedlist:
    '''
    Linked list class
    Every linked list has a head node
    '''
    def __init__(self):
        self.head = None

    def __len__(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def __str__(self):
        if self.head is None:
            return ''
        l = []
        temp = self.head
        while temp:
            l.append(str(temp.data))
            temp = temp.next
        return ' '.join(l)

    def search(self, key):
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            if current_node.data == key:
                return True
        return False

    def insert_at_head(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        node.next = self.head
        self.head = node

    def insert_at_tail(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = node

    def insert_before_key(self, key, data):
        if self.head is None:
            return
        if self.head.data == key:
            self.insert_at_head(data)
            return
        temp = self.head
        while temp.next is not None:
            if temp.next.data == key:
                node = Node(data)
                node.next = temp.next
                temp.next = node
                return
            temp = temp.next
        return

    def insert_after_key(self, key, data):
        if self.head is  None:
            return
        temp = self.head
        while temp is not None:
            if temp.data == key:
                node = Node(data)
                node.next = temp.next
                temp.next = node
                return
            temp = temp.next
        return

    def remove_from_head(self):
        current_head = self.head
        if self.head.next is None:
            return
        else:
            self.head = current_head.next
            del current_head

    def remove_from_tail(self):
        current_head = self.head
        if current_head is None:
            return
        elif current_head.next is None:
            del current_head
            self.head = None
            return
        else:
            temp = self.head
            temp2 = self.head.next
            while temp2.next is not None:
                temp = temp.next
                temp2 = temp2.next
            temp.next = None
            del temp2

    def remove_by_key(self, key):
        if self.head is None:
            return
        if self.head == key:
            self.head = None
            return
        temp = self.head
        while temp.next is not None:
            if temp.next.data == key:
                temp.next = temp.next.next
                del temp.next
        return

    def remove_before_key(self, key):
        if self.head is None or self.head.next is None:
            return
        temp1 = self.head
        temp2 = self.head.next
        if temp2.data == key:
            self.head = temp2
            del temp1
            return
        while temp2.next is not None:
            if temp2.next.data == key:
                temp1.next = temp2.next
                del temp2
                return
            temp1 = temp1.next
            temp2 = temp2.next

    def remove_after_key(self, key):
        if self.head is None or self.head.next is None:
            return
        temp1 = self.head
        temp2 = self.head.next
        if temp1.data == key:
            temp1.next = temp2.next
            del temp2
            return
        while temp2 is not None:
            if temp1.data == key:
                temp1.next = temp2.next
                del temp2
                return
            temp1 = temp1.next
            temp2 = temp2.next

    def update(self, key, data):
        temp = self.head
        while temp is not None:
            if temp.data == key:
                temp.data = data
            temp = temp.next
        return

    def remove_kth_node(self, k):
        head = self.head
        if head is None: return;
        if k == 0:
            if head.next is not None:
                self.head = head.next
                del head
                return
            del head
        c = 1
        temp = self.head
        while temp is not None:
            if c == k:
                if temp.next is not None:
                    temp.next = temp.next.next
                    n = temp.next
                    del n
                return
            temp = temp.next
            c += 1

    def combine(self, list1, list2):
        if list1.head is None and list2.head is None:
            return self
        if list1.head is None and list2.head is not None:
            self.head = list2.head
            head = list2.head
            last = self.head
            while head is not None:
                list2.head = head.next
                last.next = list2.head
                last = last.next
                head = head.next
            return self
        if list2.head is None and list1.head is not None:
            self.head = list1.head
            head = list1.head
            last = self.head
            while head is not None:
                list1.head = head.next
                last.next = list1.head
                last = last.next
                head = head.next
            return self
        self.head = list1.head
        head = list1.head
        last = self.head
        while head.next is not None:
            list1.head = head.next
            last.next = list1.head
            last = last.next
            head = head.next
        list1.head = head.next
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = list2.head
        last = last.next
        head = list2.head
        while head.next is not None:
            list2.head = head.next
            last.next = list2.head
            last = last.next
            head = head.next
        list2.head = head.next
        return self

    def remove_duplicates(self):
        elems = [self.head.data]
        if self.head is None or self.head.next is not None:
            return
        temp = self.head
        while temp.next is not None:
            if temp.next.data in elems:
                temp.next = temp.next.next
            elems.append(temp.data)
        return self

    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_to_current = current.next
            current.next = previous
            previous = current
            current = next_to_current
        self.head = previous

    def middle_node(self):
        if self.head is None:
            return ''
        if self.head.next is None:
            return self.head.data
        if len(self) % 2:
            slow = self.head
            fast = self.head
            while fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow.data
        else:
            slow = self.head
            fast = self.head.next
            while fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow.data, slow.next.data

    def display_helper(self, node):
        if node is None:
            return
        print(node.data, end=' ')
        return self.display_helper(node.next)

    def display(self):
        if self.head is None:
            return
        return self.display_helper(self.head)


lst = Linkedlist()
lst.insert_at_tail(1)
lst.insert_at_tail(2)
lst.display()

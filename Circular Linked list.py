class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is None:
            return ''
        l = []
        temp = self.head
        while temp.next != self.head:
            l.append(str(temp.data))
            temp = temp.next
        l.append(str(temp.data))
        return ' '.join(l)

    def __len__(self):
        if self.head is None: return 0;
        n = 1
        temp = self.head
        while temp.next != self.head:
            n += 1
            temp = temp.next
        return n

    def insert_at_head(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            node.next = node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = node
            node.next = self.head
            self.head = node

    def insert_at_tail(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            node.next = node
            return
        temp = self.head
        while temp.next is not self.head:
            temp = temp.next
        temp.next = node
        node.next = self.head

    def search(self, to_search):
        if self.head is None:
            return False
        temp = self.head
        while temp.next is not self.head:
            if temp.data == to_search:
                return True
            temp = temp.next
        return False

    def remove_head(self):
        if self.head is None:
            return
        if self.head.next is self.head:
            head = self.head
            self.head = None
            del head
            return
        temp = self.head
        while temp.next is not self.head:
            temp = temp.next
        old_head = self.head
        temp.next = self.head.next
        self.head = self.head.next
        del old_head

    def remove_tail(self):
        if self.head is None:
            return
        if self.head.next is self.head:
            tail = self.head
            self.head = None
            del tail
        temp = self.head
        while temp.next.next is not self.head:
            temp = temp.next
        tail = temp.next
        temp.next = self.head
        del temp

    def insert_after_key(self, key, data):
        new_node = Node(data)
        if self.head is None:
            return
        if self.head.next is self.head and self.head.data != key:
            return
        temp = self.head
        while temp.next is not self.head:
            if temp.data == key:
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
        if temp.data == key:
            new_node.next = temp.next
            temp.next = new_node
            return

    def insert_before_key(self, key, data):
        new_node = Node(data)
        if self.head is None: return
        if self.head.data == key:
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        while temp.next is not self.head:
            if temp.next.data == key:
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next


lst = CircularLinkedList()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node

    def insert_at_tail(self, data):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
            return
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def __str__(self):
        lst = []
        if self.head is None:
            return ''
        temp = self.head
        while temp is not None:
            lst.append(str(temp.data))
            temp = temp.next
        return ' '.join(lst)

    def __len__(self):
        if self.head is None:
            return 0
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count

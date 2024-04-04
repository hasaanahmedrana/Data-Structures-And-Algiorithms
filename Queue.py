class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    SIZE = 0
    def __init__(self):
        self.head = None
        self.tail = None
    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        Queue.SIZE += 1
    def dequeue(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            Queue.SIZE -= 1
            return popped
    def is_empty(self):
        return self.head is None
    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.data
    def display(self):
        if self.is_empty():
            return ''
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return 'Queue: ' + ' '.join(elements)
    def __len__(self):
        return Queue.SIZE
    def __str__(self):
        return self.display()
    def __repr__(self):
        return self.display()

def main():
    q = Queue()
    print(len(q))
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q)
    print(len(q))
    print(q.dequeue())
    print(q)
main()
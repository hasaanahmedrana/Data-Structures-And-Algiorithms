class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    SIZE = 0
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        Stack.SIZE += 1

    def pop(self):
        if self.is_empty():
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            Stack.SIZE -= 1
            return popped

    def is_empty(self):
        return self.head is None

    def peek(self):
        if self.is_empty():
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
        return 'Stack: ' + ' '.join(elements)

    def __len__(self):
        return Stack.SIZE

    def __str__(self):
        return self.display()

    def __repr__(self):
        return self.display()


def main():
    s = Stack()
    print(len(s))
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    print(s)
    print(s.pop())
    print(s.pop())
    print(s)
    print(s.peek())
    print(s.is_empty())
    print(len(s))

if __name__ == '__main__':
    main()

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = self.rear = 0

    def enqueue(self, num):
        if self.is_full():
            print('FULL')
            return
        if self.queue[self.rear] is None:
            self.queue[self.rear] = num
        elif self.queue[self.rear] is not None:
            if self.rear != self.size - 1:
                self.queue[self.rear+1] = num
                self.rear += 1
            elif self.queue[0] is None:
                self.queue[0] = num
                self.rear = 0

    def dequeue(self):
        if self.front != self.size - 1:
            n = self.queue[self.front]
            self.queue[self.front] = None
            self.front += 1
            return n
        elif self.front != self.size:
            n = self.queue[self.front]
            self.queue[self.front] = None
            self.front += 1
            return n

    def display(self):
        print('Elements in Circular Queue are:', end=' ')
        if self.front < self.rear:
            for i in range(self.front, self.rear+1):
                print(self.queue[i], end=' ')
        else:
            for i in range(self.front, self.size):
                print(self.queue[i], end=' ')
            for i in range(0, self.rear+1):
                print(self.queue[i], end=' ')
        print()

    def give_front(self):
        return self.queue[self.front]

    def give_rear(self):
        return self.queue[self.rear]

    def is_full(self):
        return self.front == 0 and self.rear == self.size - 1

    def is_empty(self):
        return self.front == 0 and self.rear == 0 and self.queue[0] is None


if __name__ == "__main__":
    ob = CircularQueue(5)
    print(ob.is_empty())
    ob.enqueue(14)
    ob.enqueue(22)
    ob.enqueue(13)
    ob.enqueue(-6)
    print(ob.is_full())
    print(ob.is_empty())
    ob.display()
    print("Deleted value = ", ob.dequeue())
    print("Deleted value = ", ob.dequeue())
    ob.display()
    ob.enqueue(9)
    ob.enqueue(20)
    ob.enqueue(5)
    ob.display()

'''
Heap:
    - A complete binary tree
    - Two types: Min Heap and Max Heap
    - Min Heap: The value of the root node is less than or equal to either of its children
    - Max Heap: The value of the root node is greater than or equal to either of its children
    - Heap is used to implement priority queue
    - Operations:
        - Insertion
        - Deletion
        - Heapify
        - Build Heap (creation of heap by heapify take O(n) time else O(nlog(n)))
    - Time Complexity:
        - Insertion: O(1) to  O(log(n))
        - Deletion: O(log(n))
        - Heapify: O(n)
        - Build Heap: O(n)
    - Space Complexity: O(n)
    - Applications:
        - Heap Sort (creation of heap and then deletion of elements) so O(nlog(n))
        - Priority Queue
        - Graph Algorithms
        - Dijkstra's Algorithm
        - Prime's Algorithm
        - Huffman Coding
        - Merge Sort
        - Order Statistics
        - Median of a stream
--> Maximum number of nodes in a binary tree with height h is "2^(h+1) - 1"
--> Minimum number of nodes in a binary tree with height h is "h + 1"

'''


class Minheap:
    def __init__(self):
        self.arr = [None]
        self.size = 0

    def display_heap(self):
        print(self.arr[1:])

    def get_size(self):
        return self.size

    def left_child(self, i):
        if (2 * i) < self.size and i > 0:
            return self.arr[i * 2]
        else:
            return None
    def right_child(self, i):
        if ((i * 2) + 1) < self.size and i > 0:
            return self.arr[(i * 2) + 1]
        else:
            return None

    def parent(self, i):
        if i > 1 and i <= self.size:
            return self.arr[i // 2]
        else:
            return None

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def peek(self):
        if self.size > 0:
            return self.arr[1]

    def is_empty(self):
        return self.size == 0

    def insert(self, value):
        self.arr.append(value)
        self.heapify_up()
        self.size += 1

    def delete(self):
        if self.size == 0: return;
        root = self.arr[1]
        self.swap(1, self.size)
        self.arr.pop()
        self.heapify_down()
        self.size -= 1
        return root

    def heapify_up(self):
        idx = self.size
        while True:
            if idx <= 1: return
            if self.arr[idx] > self.parent(idx): return
            self.swap(idx, idx // 2)
            idx = idx // 2

    def heapify_down(self):
        idx = 1
        while True:
            l = self.left_child(idx)
            r = self.right_child(idx)

            if not l and not r:
                return
            elif not r and l:
                if self.arr[idx] <= l: return
                self.swap(idx, idx * 2)
                idx = idx * 2
            elif l and r:
                mini = min(l, r)
                if self.arr[idx] <= mini:
                    return
                else:
                    if mini == l:
                        self.swap(idx, idx * 2)
                        idx = idx * 2
                    else:
                        self.swap(idx, (idx * 2) + 1)
                        idx = (idx * 2) + 1

    def heapsort(self):
        lst = []
        while self.size > 0:
            lst.append(self.delete())
        return lst


if __name__ == '__main__':
    heap = Minheap()
    heap.insert(10)
    heap.insert(20)
    heap.insert(30)
    heap.insert(40)
    heap.insert(50)
    heap.insert(60)
    heap.insert(70)
    heap.insert(80)
    heap.insert(90)
    heap.insert(100)
    heap.display_heap()
    print(heap.peek())
    heap.delete()
    heap.display_heap()
    heap.delete()
    heap.display_heap()
    heap.delete()
    heap.display_heap()
    heap.delete()
    heap.display_heap()
    heap.delete()
    heap.display_heap()
    heap.delete()
    heap.display_heap()
    heap.delete()
    heap.display_heap()
    heap.delete()
    heap.display_heap()
    heap.delete()
    heap.display_heap()
    heap.delete()
    heap.display_heap()


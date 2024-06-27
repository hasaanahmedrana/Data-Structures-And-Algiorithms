'''Implementation of maxheap by heapify method which have time complexity od O(n) to build heap'''

class MaxHeap:
    def __init__(self, arr):
        self.size = len(arr)
        self.arr =  [None] + arr
        self.build()

    def build(self):
        for i in range(self.size//2,0,-1):
            self.heapify_down(i)

    def swap(self, m, n):
        self.arr[m],self.arr[n] = self.arr[n],self.arr[m]

    def heapify_down(self, idx=1):
        largest = idx
        left = idx*2
        right = (idx*2)+1
        if left < self.size and self.arr[left] > self.arr[largest]:
            largest = left

        if right < self.size and self.arr[right] > self.arr[largest]:
            largest = right

        if largest != idx:
            self.swap(idx, largest)
            self.heapify_down(largest)

    def __str__(self):
        lst = self.arr[1:self.size + 1]
        if lst==[]: return '[]'
        s = ','.join(map(str, lst))
        return s

    def peek(self):
        return self.arr[1] if self.size > 0 else None

    def delete(self):
        if self.size > 0:
            root = self.peek()
            self.swap(1,self.size)
            self.size -= 1
            self.heapify_down()
            return root


    def heap_sort(self):
        for i in range(self.size + 1):
            self.delete()
        return self.arr[1:]


def main():
    l = [4,7,1,8,10,2,9,3,6,5]
    heap = MaxHeap(l)
    print(heap)
    print(heap.heap_sort())
    print(heap)
main()


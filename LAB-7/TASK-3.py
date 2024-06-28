import random
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def insert(self, value):
        hash = value % self.size
        if self.table[hash] is None:
            self.table[hash] = value
            return True
        else:
            return False

def getRandom():
    return random.randint(1, 101)

def check(size, num_trials):
    total = 0
    for _ in range(num_trials):
        table = HashTable(size)
        num_insertions = 0
        while True:
            value = getRandom()
            if table.insert(value):
                num_insertions += 1
            else:
                break
        total += num_insertions
    return total / num_trials

if __name__ == '__main__':
    num_trials = 50
    for size in range(10, 101, 10):
        avg_insertions = check(size, num_trials)
        print(f"{size}: Average insertions is {avg_insertions}")
print('------TASK-1--------')
'''Convert decimal to Octal'''

def dec_to_oct(n:int) -> str:
    if n <= 0:
        return ''
    return dec_to_oct(n//8) + str(n % 8)

print(dec_to_oct(80))
print(dec_to_oct(10))
print(dec_to_oct(23))
print('-' * 20)


print('------TASK-2--------')
'''Pascal Triangle recursively'''
def pascals_triangle(lst:list, n:int, i:int):
    if n == i:
        return lst
    if i == 0:
        lst.append([1])
    else:
        temp = [1] + [(lst[-1][i] + lst[-1][i+1]) for i in range(len(lst[-1])-1)] + [1]
        lst.append(temp)
    return pascals_triangle(lst, n, i + 1)
n = int(input('Enter the number of rows: '))
print(pascals_triangle([], n, 0))
print('-' * 20)


print('-----TASK-3------')
''' For GOOD string, each element of the list is a string  of digits in which 
    digits at odd indexes are even and digits at even indexes are  prime number.'''

def is_prime(n:int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_string(s:str) -> bool:
    print(s)
    if len(s) == 1:
        return int(s[0]) % 2 == 0
    elif len(s) == 0:
        return True
    elif len(s) == 2:
        return int(s[0]) % 2 != 0 or not is_prime(int(s[1]))
    else:
        return check_string(s[2:])

def main():
    s = input('Enter string: ')
    print('GOOD' if not check_string(s) else 'NOT GOOD')
if '__name__' == '__main__':
    main()

print('------TASK-4--------')
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = Node()

    def display(self) -> list:
        current_node = self.head
        lst = []
        while current_node.next is not None:
            current_node = current_node.next
            lst.append(current_node.data)
        return lst

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def search(self, key):
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            if current_node.data == key:
                return True
        return False

    def insert_after(self, key, data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next != None:
            if current_node.data == key:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next
        if current_node.data == key:
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print('Key does not exist')

    def insert_before(self, key, data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next.data != key:
            if current_node.next == None:
                return
            current_node.next = current_node.next
        temp = current_node.next
        new_node.next = temp
        current_node.next = new_node


lst = Linkedlist()
lst.insert_at_tail(5)
lst.insert_at_tail(4)
lst.insert_at_tail(3)
lst.insert_at_head(2)
lst.insert_at_head(1)
print(lst.display())
lst.insert_after(2, 7)
lst.insert_after(3, 7)
lst.insert_before(1, 0)
lst.insert_before(0, 23)
print(lst.display())

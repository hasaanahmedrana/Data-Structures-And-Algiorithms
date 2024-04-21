from time import time
"""
WHAT IS RECURSION?
Recursion is a technique in which a function calls itself in order to solve a problem.
Recursion is a powerful tool for solving problems that can be defined in terms of similar sub-problems.
It follows divide and conquer approach.
"""

# Iteratively calculating the fibonacci series
lst = [0, 1]
def fibonacci_iteratively(n):
    for i in range(n+1):
        print(lst[-2])
        lst.append(lst[-1] + lst[-2])
t1 = time()
fibonacci_iteratively(35)
iterative_time = time() - t1
print('-' * 20)

# Recursively calculating the fibonacci series
def fibonacci(n):
    if not isinstance(n, int):
        raise TypeError('n must be a positive integer')
    if n < 0:
        raise ValueError('n must be a positive integer')
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

t2 = time()
for i in range(35):
    print(i+1, ':', fibonacci(i))
recursive_time = time() - t2
print('-'*20)

"""--- OPTIMIZATION OF RECURSIVE PROBLEMS (MEMOIZATION) is vert important as it can be very slow.--- 
-> The Time complexity of iterative function is O(n) which is very fast.
-> The space complexity of iterative function is O(1) which is also very fast.
-> The time complexity of the recursive function is O(2^n) which is very slow.
-> The space complexity of the recursive function is O(n) which is also very slow.
-> The time complexity of the optimized recursive function is O(n) which is very fast.
-> The space complexity of the optimized recursive function is O(1) which is also very fast.
"""

fibonacci_cache = {}
def fibonacci(n):
    if not isinstance(n, int):
        raise TypeError('n must be a positive integer')
    if n < 0:
        raise ValueError('n must be a positive integer')
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n == 0 or n == 1:
        return n
    value = fibonacci(n - 1) + fibonacci(n - 2)
    fibonacci_cache[n] = value
    return value

t3 = time()
for i in range(35):  # try to find same value of fibonacci(1000) without using cache it will be very slow.
    print(i+1, ':',fibonacci(i))
optimized_recursive_time_with_cache = time() - t3
print('-' * 20)

''' First Code without memorization will be very slow for large n values. So we can use LRU Cache to optimize the code.
    LRU Cache: LEAST RECENTLY USED  Cache. (Provides oen line way to add memorization to a recursive function)
    By default the cache size is 128 But you can change it as needed.'''
from functools import lru_cache
@lru_cache(maxsize=1000)
def fibonacci(n):
    if not isinstance(n, int):
        raise TypeError('n must be a positive integer')
    if n < 0:
        raise ValueError('n must be a positive integer')
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

t4 = time()
for i in range(35):
    print(i+1, ':', fibonacci(i))   # This will be very fast as compared to the first code without memorization.
optimized_recursive_time_with_lru_cache = time() - t4

print('-' * 20)
print()

'''     Time simply shows that simple recursive function takes alot of time probably 10-20 times of iterative approach.
        But when we use memorization in recursive function it takes almost same time as iterative function.
        And when we use LRU Cache in recursive function it takes almost same time as iterative function
        Recursive Approach time >>>>> (Iterative time , Optimized recursive time).'''

print(f'Iterative Time: {iterative_time}')
print(f'Recursive Time: {recursive_time}')
print(f'Optimized Recursive Time with Cache: {optimized_recursive_time_with_cache}')
print(f'Optimized Recursive Time with LRU Cache: {optimized_recursive_time_with_lru_cache}')



'''
ADVANTAGES/DISADVANTAGES OF RECURSION:
Advantages:
 -> Simplicity: Recursion makes code shorter, cleaner and easier to maintain. 
 -> Reduced Variables: With recursion, you can solve complex problems without the need to use many variables. 
    The state of each recursive call is kept on the system stack.
-> Problem Solving: Recursion is a powerful tool for solving problems that can be defined in terms of similar sub-problems.
    For instance, merge sort and quick sort are recursive sorting algorithms.
-> Recursion is used in many algorithms such as tree traversal, graph traversal, and divide-and-conquer algorithm.

Disadvantages:
-> Infinite Recursion: When a recursive function calls itself infinitely, it leads to infinite recursion.
-> Stack Overflow: When the recursion depth exceeds the maximum recursion depth, it leads to stack overflow.
-> Memory Consumption: Recursion consumes more memory than iteration because each recursive call adds a new layer to the stack.
-> Performance: Recursion is slower and less efficient than iteration because of the overhead of function calls.
-> Debugging: Recursion is harder to debug than iteration because of the complex call stack.
-> Complexity: Recursion is harder to understand than iteration because of the complex call stack.
-> Tail Recursion: In some programming languages, tail recursion is optimized by the compiler. 
    But in python, tail recursion is not optimized by the compiler. 
    So, you should avoid tail recursion in python to prevent stack overflow.
'''

''' PITFALLS IN RECURSION:
-> No base Case.
-> Wrong Base Case
-> Forget to return
'''





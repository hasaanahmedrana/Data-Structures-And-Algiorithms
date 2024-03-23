# Palindrome: to check if the string is palindrome or not
def palindrome(s):
    if len(s) == 1 or s == '':
        return True
    if s[0]!=s[-1]:
        return False
    else:
        return palindrome(s[1:-1])

print(palindrome('naan'))     #EXPECTED ANS -- TRUE
print(palindrome('abc'))      #EXPECTED ANS -- FALSE
print(palindrome('abcdcba'))  #EXPECTED ANS -- TRUES
print(palindrome('abcddcba')) #EXPECTED ANS -- TRUE
print(palindrome('abcdecba')) #EXPECTED ANS -- FALSE

# Factorial: to find the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
print(factorial(5))     #EXPECTED ANS -- 120
print(factorial(6))     #EXPECTED ANS -- 720
print(factorial(7))     #EXPECTED ANS -- 5040


# Fibonacci: to find the nth number in the fibonacci series
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))     #EXPECTED ANS -- 5
print(fibonacci(6))     #EXPECTED ANS -- 8
print(fibonacci(7))     #EXPECTED ANS -- 13


# Reverse: to reverse a string
def reverse(s):
    if s == '':
        return ''
    return s[-1] + reverse(s[:-1])
print(reverse('abcd'))     #EXPECTED ANS -- dcba
print(reverse('abcde'))    #EXPECTED ANS -- edcba
print(reverse('abcdef'))   #EXPECTED ANS -- fedcba


# Binary Search: to find the number in the list
def binary_search(lst, n):
    lst.sort()
    lower = 0
    upper = len(lst)-1
    mid = (upper + lower) // 2
    if n == lst[mid] or n == lst[upper] or n == lst[lower]:
        return True
    if upper-lower == 1:
        return False
    if n > lst[mid]:
        return binary_search(lst[mid+1:], n)
    if n < lst[mid]:
        return binary_search(lst[:mid+1], n)

print(binary_search([1, 3, 4, 5, 99, 23, 566, 5], 56))       #EXPECTED ANS -- FALSE
print(binary_search([2, 3, 5, 68, 97, 5, 12, 55, 1, 88], 55))  #EXPECTED ANS -- TRUE
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8], 3))            #EXPECTED ANS -- TRUE
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 12, 35, 12231, 3443, 12132, 323, 23, 134, 99, 101],  100))   #EXPECTED ANS -- FALSE
print('-'*20)

# Decimal into binary conversion
def dec_to_bin(n):
    if n <= 0:
        return ''
    return dec_to_bin(n//2) + str(n % 2)
print(dec_to_bin(3))
print(dec_to_bin(12))
print(dec_to_bin(23))
print('-' * 20)

def dec_to_bin(n):
    if n == 0:
        return
    dec_to_bin(n // 2)
    print(n % 2, end='')
dec_to_bin(13)
print()

#DECIMAL INTO REVERSE BINARY conversion
def dec_to_reverse_bin(n):
    if n == 0:
        return
    print(n % 2, end='')
    dec_to_reverse_bin(n // 2)
dec_to_reverse_bin(13)
print()
print('-' * 20)

#TO FIND IF THE SUM OF ANY TWO LIST ELEMENT IS EQUALS TO 'N' NUMBER
#my approach
def searching_pair(arr, n, mid):
    if len(arr) <= 1:
        return False
    if arr[-1] <= mid:
        return False
    elif n - arr[-1] in arr[:-1]: return True
    return searching_pair(arr[:-1], n, mid)
def sum_of_2_is_n(arr, n):
    if n >= arr[-1] * 2 or n <= arr[0]:
        return False
    mid = n / 2
    return searching_pair(arr, n, mid)
lst = [1, 2, 3, 4, 5, 6]
num = 5
print(sum_of_2_is_n(lst, num))
print('-' * 20)

# SIR ABDULLAH'S APPROACH
def searching_pair(arr, n, i, j):
    if i == j:
        return False
    if arr[i] + arr[j] == n:
        return True
    elif arr[i] + arr[j] > n:
        return searching_pair(arr, n, i, j - 1)
    else:
        return searching_pair(arr, n, i + 1, j)
def sum_of_2_is_n(arr, n):
    if n >= arr[-1] * 2 or n <= arr[0]:
        return False
    i = 0
    j = len(arr) - 1
    return searching_pair(arr, n, i, j)
lst = [1, 3, 5, 6]
num = 9
print(sum_of_2_is_n(lst, num))

# To find the pascal triangle
def pascal_triangle(n):
    if n == 0:
        return [1]
    else:
        previous_row = pascal_triangle(n-1)
        print(previous_row)
        new_row = [1] + [previous_row[i] + previous_row[i+1] for i in range(len(previous_row)-1)] + [1]
    return new_row
print(pascal_triangle(5))
print('-' * 20)

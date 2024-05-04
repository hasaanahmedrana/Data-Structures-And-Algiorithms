import time
import random


def bubblesort(lst: list):
    """
    SIMPLEST SORTING ALGORITHM: it compares two adjacent elements
    and swaps them if they are in the wrong order until the entire list is sorted.
    In each iteration, the largest element is moved to the end of the list.
    Complexity: O(n^2) average case, O(n^2) worst case Best case O(n)
    Space: O(1)
    Stable sort: Yes
    In-place: Yes
    video link: https://www.youtube.com/watch?v=lyZQPjUT5B4
    """
    n = len(lst)
    for i in range(1, n):
        for j in range(n-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


x = [3, 4, 1, 6, 9, 6, 0]
print(bubblesort(x))


def insertion_sort(arr: list):
    '''It builds the final sorted list one item at a time.
    It takes each element from the list and inserts it into its correct position in the sorted list.
    Complexity: O(n^2) average case, O(n^2) worst case
    Space: O(1)
    video link: https://www.youtube.com/watch?v=JU767SDMDvA
    Stable sort: Yes
    In-place: Yes
    '''
    for i in range(1, len(arr)):
        for j in range(i-1, -1, -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                break
    return arr


x = [3, 4, 1, 6, 9, 6, 0, 99, 1, 3, 99, 2, 323, 12, 23, 11, 12, 345, 686]
print(insertion_sort(x))


def selection_sort(lst: list):
    """
    It selects the smallest element from the unsorted portion of the list
    and swaps it with the first element of the unsorted portion of the list.
    Complexity: O(n^2) average case, O(n^2) worst case
    Space: O(1)
    video link: https://www.youtube.com/watch?v=g-PGLbMth_g
    """
    n = len(lst)
    for i in range(n):
        mini = i
        for j in range(i, n):
            curr = lst[j]
            if curr < lst[mini]:
                mini = j
        lst[i], lst[mini] = lst[mini], lst[i]
    return lst


def insertion_sort(arr: list):
    '''It builds the final sorted list one item at a time.
    It takes each element from the list and inserts it into its correct position in the sorted list.
    Complexity: O(n^2) average case, O(n^2) worst case
    Space: O(1)
    video link: https://www.youtube.com/watch?v=JU767SDMDvA
    Stable sort: Yes
    In-place: Yes

    '''
    for i in range(1, len(arr)):
        for j in range(i-1, -1, -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                break
    return arr


def partition(lst: list, lb: int, ub: int) -> int:
    '''
    This function takes first element as pivot (we can also choose last or any random element as pivot)
    , places the pivot element at its correct position in sorted array,
    and places all smaller (smaller than pivot) to left of pivot and all greater elements to right of pivot.
    It returns the correct index of that pivot element in sorted array'''
    start = lb
    end = ub
    pivot = lst[lb]
    while start < end:
        while lst[start] <= pivot and start < end:
            start += 1
        while lst[end] > pivot:
            end -= 1
        if start < end:
            lst[start], lst[end] = lst[end], lst[start]
    lst[lb], lst[end] = lst[end], lst[lb]
    return end


def quick_sort(lst: list, lb: int, ub: int) -> list[int]:
    '''
    QUICK SORT:
    The main function that implements QuickSort. It takes a list, a starting index, and an ending index
    as input and returns the sorted list.
    It uses divide and conquer strategy to sort the array recursively.
    It get one element and places it in its correct position in the sorted array and then call
    partition for left and right partitions of list

    Complexity: O(nlogn) average case, O(n^2) worst case
    Space: O(logn) average case, O(n) worst case
    In-place: Yes
    Stable: No
    Video link: https://www.youtube.com/watch?v=QN9hnmAgmOc
    '''
    if lb < ub:
        m = partition(lst, lb, ub)
        quick_sort(lst, lb, m-1)
        quick_sort(lst, m+1, ub)
    return lst


x = [34, 5, 7, 8, 22, 1]
print(quick_sort(x, 0, len(x)-1))


def merge(arr1: list, arr2: list) -> list:
    '''MERGE: It takes two sorted arrays and merges them into a single sorted array.
    Complexity: O(n) average case, O(n) worst case
    Space: O(n)'''
    result = [0] * (len(arr1) + len(arr2))
    i = 0
    j = 0
    k = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result[k] = arr1[i]
            i += 1
        else:
            result[k] = arr2[j]
            j += 1
        k += 1
    while i < len(arr1):
        result[k] = arr1[i]
        i += 1
        k += 1
    while j < len(arr2):
        result[k] = arr2[j]
        j += 1
        k += 1
    return result


def merge_sort(arr):
    '''MERGE SORT: It divides the input array into two halves, calls itself for the two halves,
    and then merges the two sorted halves.
    It uses divide and conquer strategy to sort the array recursively.
    Follow left order traversal: left subtree, right subtree, root
    Complexity: O(nlogn) average case, O(nlogn) worst case
    Space: O(n)
    Video link: https://www.youtube.com/watch?v=ak-pz7tS5DE
    Stable sort: Yes
    In place: No

    ADVANTAGE:
    -> It is suitable for large size arrays
    -> It is suitable for linked lists.
    -> It supports external sorting.
    -> It is stable (the original order of duplicate elements is maintained)
    DISADVANTAGE:
    -> It is not in-place (it requires extra space) (BUT NOT IN CASE OF LINKED LIST)
    -> It is not suitable for small size arrays. We'll go for insertion sort because it is also Stable as merge sort.
    -> It is recursive and involves multiple function calls.
    '''

    if len(arr) <= 1: return arr
    mid = len(arr)//2
    lst1 = merge_sort(arr[:mid])
    lst2 = merge_sort(arr[mid:])
    return merge(lst1, lst2)


print(merge_sort([11, 34, 5, 6, 21, 5, 2, 3]))


def counting_sort(arr: list[int]):
    """
    COUNTING SORT:
    It is not a comparison based sorting algorithm.
    It is a sorting technique based on keys between a specific range.
    It works by counting the number of objects having distinct key values (kind of hashing).
    Then doing some arithmetic to calculate the position of each object in the output sequence.
    Complexity: O(n+k) average case, O(n+k) worst case
    Space: O(n+k)
    Stable Sort: Yes
    In place: No
    Video link: https://www.youtube.com/watch?v=OKd534EWcdk
    """
    frequency = [0] * (max(arr)+1)
    result = [0] * len(arr)
    for num in arr:
        frequency[num] += 1

    for i in range(1, len(frequency)):
        frequency[i] += frequency[i-1]

    for i in range(len(frequency)):
        frequency[i] -= 1
    for each in range(len(arr)-1, -1, -1):
        result[frequency[arr[each]]] = arr[each]
        frequency[arr[each]] -= 1
    return result


l = [random.randint(0, 10000000) for i in range(1000000)]
t1 = time.time()
print(counting_sort(l))
x = time.time() - t1


def frequencysort(arr):
    '''If the K(highest element) size is very large then this code is much more efficient than
    counting sort else counting sort will be efficient than this one
    '''
    count = {}
    for i in arr:
        count[i] = count.get(i, 0) +1
    result = []
    for i, j in sorted(count.items()):
        result += ([i]*j)
    return result


t2 = time.time()
print(frequencysort(l))
y = time.time() - t2
t3 = time.time()
print(merge_sort(l))
z = time.time() - t3
print(x, y, z)


# def merge_sort_recursive(arr: list) -> list[int]:
#     if len(arr) == 1:
#         return arr
#
#     arr_one = arr[:len(arr)//2]
#     arr_two = arr[len(arr)//2:]
#     arr_one = merge_sort_recursive(arr_one)
#     arr_two = merge_sort_recursive(arr_two)
#     return merge(arr_one, arr_two)
#
#
# def merge(arr1: list, arr2: list):
#     '''It divides the input array into two halves, calls itself for the two halves,
#     and then merges the two sorted halves.
#     It uses divide and conquer strategy to sort the array recursively.
#     Complexity: O(nlogn) average case, O(nlogn) worst case
#     Space: O(n)
#     video link: https://www.youtube.com/watch?v=JSceec-wEyw
#     '''
#     arr = []
#     while len(arr1) > 0 and len(arr2) > 0:
#         if arr1[0] < arr2[0]:
#             arr.append(arr1[0])
#             arr1.pop(0)
#         else:
#             arr.append(arr2[0])
#             arr2.pop(0)
#     for i in arr1:
#         arr.append(i)
#     for i in arr2:
#         arr.append(i)
#     return arr
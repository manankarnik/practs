from typing import List

def bubble_sort(arr: List[int]) -> List[int]:
    arr = arr.copy()
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped: break
    return arr


def selection_sort(arr: List[int]) -> List[int]:
    arr = arr.copy()
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]: min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr: List[int]) -> List[int]:
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1: return arr
    arr = arr.copy()
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
    

def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1: return arr
    arr = arr.copy()
    left = merge_sort(arr[:len(arr)//2])
    right = merge_sort(arr[len(arr)//2:])

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
        
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
print("Original:", arr)
sorted_arr = merge_sort(arr)
print("Sorted:", sorted_arr)

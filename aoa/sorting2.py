from typing import List
from random import sample, random

def counting_sort(arr):
    arr = arr.copy()
    counts = [0] * (max(arr) + 1)
    
    for i in arr:
        counts[i] += 1

    arr = []
    # for i, count in enumerate(counts):
    #     arr.extend([i] * count)

    for i in range(len(counts)):
        while counts[i] > 0:
            arr.append(i)
            counts[i] -= 1
        
    return arr


def radix_cs(arr, exp):
    arr = arr.copy()
    output = [0] * len(arr)
    counts = [0] * 10

    for i in arr:
        counts[i // exp % 10] += 1

    for i in range(1, 10):
        counts[i] += counts[i - 1]

    for item in reversed(arr):
        idx = item // exp % 10
        output[counts[idx] - 1] = item
        counts[idx] -= 1
    return output


def radix_sort(arr):
    arr = arr.copy()
    exp = 1
    while max(arr) // exp > 0:
        arr = radix_cs(arr, exp)
        exp *= 10
    return arr


def bucket_sort(arr):
    arr = arr.copy()
    buckets = [[] for _ in range(len(arr))]

    for i in arr:
        idx = int(i * 10)
        buckets[idx].append(i)

    for i in range(len(buckets)):
        buckets[i] = sorted(buckets[i])

    k = 0
    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1
    return arr


# arr = sample(range(100), 10)
# print("Original:", arr)
# sorted_arr = counting_sort(arr)
# print("Sorted:", sorted_arr)
# sorted_arr = radix_sort(arr)
# print("Sorted:", sorted_arr)


arr = [round(random(), 3) for _ in range(10)]
print("Original:", arr)
sorted_arr = bucket_sort(arr)
print("Sorted:", sorted_arr)

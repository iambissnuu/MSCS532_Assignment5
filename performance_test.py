import random
import time
import sys
from deterministic_quicksort import deterministic_quicksort
from randomized_quicksort import randomized_quicksort

sys.setrecursionlimit(20000)

def time_sort(func, arr):
    start = time.time()
    func(arr.copy())
    end = time.time()
    return round((end - start) * 1000, 2)

size = 10000
random_array = random.sample(range(size * 2), size)
sorted_array = list(range(size))
reverse_sorted_array = list(range(size, 0, -1))
repeated_array = [5] * size

print("Performance Comparison (Sorting - in milliseconds):\n")

print("Random Array:")
print("Deterministic Quicksort:", time_sort(deterministic_quicksort, random_array))
print("Randomized Quicksort   :", time_sort(randomized_quicksort, random_array))

print("\nSorted Array:")
print("Deterministic Quicksort:", time_sort(deterministic_quicksort, sorted_array))
print("Randomized Quicksort   :", time_sort(randomized_quicksort, sorted_array))

print("\nReverse Sorted Array:")
print("Deterministic Quicksort:", time_sort(deterministic_quicksort, reverse_sorted_array))
print("Randomized Quicksort   :", time_sort(randomized_quicksort, reverse_sorted_array))

print("\nRepeated Elements Array:")
print("Deterministic Quicksort:", time_sort(deterministic_quicksort, repeated_array))
print("Randomized Quicksort   :", time_sort(randomized_quicksort, repeated_array))

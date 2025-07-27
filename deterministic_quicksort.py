def deterministic_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    return deterministic_quicksort(less) + equal + deterministic_quicksort(greater)

if __name__ == "__main__":
    sample = [8, 4, 2, 9, 5, 1, 3]
    print("Original:", sample)
    print("Sorted (Deterministic):", deterministic_quicksort(sample))

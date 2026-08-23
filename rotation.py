def left_rotate(arr, k):
    n = len(arr)
    k = k % n

    return arr[k:] + arr[:k]


arr = [1, 2, 3, 4, 5]

print(left_rotate(arr, 2))
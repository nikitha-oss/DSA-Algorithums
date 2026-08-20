arr = [10, 20, 30, 40, 50]

prefix = [0] * len(arr)

prefix[0] = arr[0]

for i in range(1, len(arr)):
    prefix[i] = prefix[i - 1] + arr[i]

print("Original array:", arr)
print("Prefix sum:", prefix)
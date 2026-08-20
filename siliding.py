arr = [1, 2, 3, 4, 5]
k = 2

window_sum = sum(arr[:k])

print(window_sum)

for i in range(k, len(arr)):
    window_sum += arr[i]
    window_sum -= arr[i - k]

    print(window_sum)
import numpy as np

rng = np.random.default_rng(seed=42)
arr = sorted([ int(i) for i in rng.integers(0, 10000, size=100)])

print(arr)

def find_idx_linear(arr, k):
    for i in range(len(arr)):
        if arr[i] == k:
            return i
    return -1

def find_idx_binary(arr, k):
    left_idx, right_idx = 0, len(arr)-1

    while left_idx <= right_idx:
        middle_idx = (left_idx + right_idx) // 2
        if k == arr[middle_idx]:
            return middle_idx
        elif k < arr[middle_idx]:
            right_idx = middle_idx - 1
        elif k > arr[middle_idx]:
            left_idx = middle_idx + 1
    return -1


nums_to_find = [438, 6545, 9756, 5555]

for num in nums_to_find:
    idx_found = find_idx_linear(arr, num)
    if idx_found == -1:
        print(f'Searching {num}, number does not exist')
    else:
        print(f'Searching {num}, found at {idx_found}')


for num in nums_to_find:
    idx_found = find_idx_binary(arr, num)
    if idx_found == -1:
        print(f'Searching {num}, number does not exist')
    else:
        print(f'Searching {num}, found at {idx_found}')



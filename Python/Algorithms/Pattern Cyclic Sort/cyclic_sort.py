def cyclicSort(arr):
    i = 0
    while i < len(arr):
        j = arr[i] - 1
        if nums[i] != nums[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1
    return arr

arr = [3, 1, 5, 4, 2]
print(cyclicSort(arr))
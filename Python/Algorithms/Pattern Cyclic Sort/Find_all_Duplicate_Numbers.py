def findAllDuplicateNumbers(arr):
    i = 0
    while i < len(arr):
        j = arr[i]-1

        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1
    print(arr)
    duplicates = []
    for i in range(len(arr)):
        if arr[i] != i+1:
            duplicates.append(arr[i])
    
    return duplicates


arr = [3, 4, 4, 5, 5]
print(findAllDuplicateNumbers(arr))
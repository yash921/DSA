# Problem Statement #

# Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.

# Example 1:

# Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
# Output: [2, 3], [5, 6], [7, 7]
# Explanation: The output list contains the common intervals between the two lists.

def intersection(arr1, arr2):
    ans = []
    i, j, start, end = 0, 0, 0, 1

    while i < len(arr1) and j < len(arr2):
        a_overlaps_b = arr1[i][start] >= arr2[j][start] and arr1[i][start] <= arr2[j][end]

        b_overlaps_a = arr2[j][start] >= arr1[i][start] and arr2[j][start] <= arr1[i][end]

        if a_overlaps_b or b_overlaps_a:
            ans.append([max(arr1[i][start], arr2[j][start]), min(arr1[i][end], arr2[j][end])])

        if arr1[i][end] < arr2[j][end]:
            i += 1
        else:
            j += 1
    return ans







arr1=[[1, 3], [5, 6], [7, 9]]
arr2=[[2, 3], [5, 7]]

print(intersection(arr1, arr2))
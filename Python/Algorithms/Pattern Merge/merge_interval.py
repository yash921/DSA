def mergeInterval(intervals):
    mergedIntervals = []
    intervals.sort(key=lambda x: x[0])

    start = intervals[0][0]
    end = intervals[0][1]

    for i in range(1, len(intervals)):
        interval = intervals[i]

        if interval[0] <= end:
            end = max(interval[1], end)
        else:
            mergedIntervals.append([start, end])
            start = interval[0]
            end = interval[1]
    
    mergedIntervals.append([start, end])
    return mergedIntervals


# intervals = [[1,4], [2,6], [3,5]]
intervals = [[4, 10], [7, 13], [16,20], [1, 40]]
print(mergeInterval(intervals))
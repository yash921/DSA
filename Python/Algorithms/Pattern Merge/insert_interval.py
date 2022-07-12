# Problem Statement #

# Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and 
# merge all necessary intervals to produce a list that has only mutually exclusive intervals.

# Example 1:

# Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
# Output: [[1,3], [4,7], [8,12]]
# Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].

def insertInterval(intervals, newInterval):
    mergedIntervals = []
    start = 0
    end = 1
    i = 0

    while i < len(intervals) and intervals[i][end] < newInterval[0]:
        mergedIntervals.append(intervals[i])
        i += 1
    
    while i < len(intervals) and intervals[i][0] <= newInterval[1]:
        newInterval[start] = min(intervals[i][0], newInterval[0])
        newInterval[end] = max(intervals[i][1], newInterval[1])
        i += 1
    mergedIntervals.append(newInterval)

    while i < len(intervals):
        mergedIntervals.append(intervals[i])
        i += 1
    return mergedIntervals

intervals=[[1,3], [5,7], [8,12], [9, 10]]
newInterval=[4,6]

print(insertInterval(intervals, newInterval))

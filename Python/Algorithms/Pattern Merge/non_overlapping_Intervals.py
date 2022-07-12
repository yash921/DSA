class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        count = 0
        start = intervals[0][0] # 1
        end = intervals[0][1] # 2
        # [[1,2], [1,3], [2,3], [3,4]]
        
        for i in range(1, len(intervals)):
            interval = intervals[i] 
            
            if interval[0] < end:  # 1 < 2
                count += 1
                
                # remove the interval with the longer end
                end = min(interval[1], end)
            else:
                end = interval[1]
                
        return count

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[1],x[0]))
        end_interval=intervals[0][1]
        remove=0
        for i in range(1,len(intervals)):
            if intervals[i][0]<end_interval:
                remove+=1
            else:
                end_interval=intervals[i][1]
        return remove
            
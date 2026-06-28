class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],-x[1]))
        n=len(intervals)
        remove=0
        end=intervals[0][1]
        for i in range(1,n):
            if intervals[i][1]<=end:
                remove+=1
            else:
                end=intervals[i][1]
        return n-remove
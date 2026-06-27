class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals)==0:
            return [newInterval]
        elif len(newInterval)==0:
            return [intervals]
        elif len(newInterval)==0 and len(intervals)==0:
            return []

        newstart=newInterval[0]
        newend=newInterval[1]
        for i in range(len(intervals),-1,-1):
            if intervals[i-1][0] <= newstart:
                intervals.insert(i,newInterval)
                break
        else:
            intervals.insert(0, newInterval)
        start = intervals[0][0]
        end = intervals[0][1]
        res=[]
        for i in range(1,len(intervals)):
            nextstart=intervals[i][0]
            nextend=intervals[i][1]
            if nextstart <= end:
                end = max(end, nextend)
            else:
                res.append([start, end])
                start=nextstart
                end=nextend
        res.append([start,end])
        return res
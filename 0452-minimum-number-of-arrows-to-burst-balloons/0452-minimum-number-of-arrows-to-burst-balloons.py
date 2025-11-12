class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:(x[1],x[0]))
        count=1
        end_points=points[0][1]
        for i in range(1,len(points)):          
            if points[i][0]>end_points:    #here, we check non intersection point and then change endpoint
                count+=1
                end_points=points[i][1]
                           
        return count
        
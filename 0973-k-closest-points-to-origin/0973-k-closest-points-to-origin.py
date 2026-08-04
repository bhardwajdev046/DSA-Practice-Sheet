# import heapq
# import math
# class pair:
#     def __init__(self,first,second):
#         self.first=first
#         self.second=second
#     def __lt__(self,other):
#         if self.first!=other.first:
#             return self.first > other.first
#         return self.second > other.second
# class Solution:
#     def distance(self,x,y):
#         return ((x*x)+(y*y))**0.5
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         heap=[]
#         for i in range(len(points)):
#             dis = self.distance(points[i][0], points[i][1])
#             curr = pair(dis, i)
#             if len(heap)<k:
#                 heapq.heappush(heap,curr)
#                 continue
#             heapq.heappush(heap,curr)
#             heapq.heappop(heap)
#         ans=[]
#         while heap:
#             ans.append(points[heapq.heappop(heap).second])
#         return ans

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            dist = point[0] * point[0] + point[1] * point[1]

            if len(heap) < k:
                heapq.heappush(heap, (-dist, point))
            else:
                heapq.heappushpop(heap, (-dist, point))

        ans = []
        while heap:
            ans.append(heapq.heappop(heap)[1])

        return ans
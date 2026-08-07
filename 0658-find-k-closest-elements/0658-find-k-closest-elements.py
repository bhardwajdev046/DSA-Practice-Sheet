import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap=[]
        for ele in arr:
            dis=abs(ele-x)
            if len(heap)<k:
                heapq.heappush(heap,(-dis,-ele))
            else:
                heapq.heappush(heap,(-dis,-ele))
                heapq.heappop(heap)
        ans=[]
        while heap:
            ans.append(-heapq.heappop(heap)[1])
        return sorted(ans)
        
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        ans=[]
        for i in stones:
            heapq.heappush(ans,-i)
        while len(ans)>1:
            stone1=-heapq.heappop(ans)
            stone2=-heapq.heappop(ans)
            res=abs(stone1-stone2)
            if res>0:
                heapq.heappush(ans,-res)
        
        if len(ans)>0:
            return -heapq.heappop(ans)
        else:
            return 0
import heapq
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        ans=[]
        for i in gifts:
            heapq.heappush(ans,-i)
        res=0
        while k>0:
            pile=-heapq.heappop(ans)
            new_pile=math.isqrt(pile)
            heapq.heappush(ans,-new_pile)
            k-=1
        return -sum(ans)
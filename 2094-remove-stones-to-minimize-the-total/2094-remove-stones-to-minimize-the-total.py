import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        arr=[]
        for i in piles:
            heapq.heappush(arr,-i) 
        while k:
            pile=-heapq.heappop(arr)
            new_pile=pile-(pile//2)
            heapq.heappush(arr,-new_pile)
            k-=1
        return -sum(arr)   
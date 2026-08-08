import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pair=[]
        n=len(profits)
        for i in range(n):
            pair.append((capital[i],profits[i]))
        pair.sort()
        heap=[]
        ind=0
        while k:
            while ind<n and pair[ind][0]<=w:
                heapq.heappush(heap,-pair[ind][1])
                ind+=1
            if len(heap)==0:
                return w
            temp=-heapq.heappop(heap)
            w+=temp
            k-=1
        return w
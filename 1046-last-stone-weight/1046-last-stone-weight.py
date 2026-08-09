class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for i in stones:
            heapq.heappush(heap, -i)
        while len(heap)>=2:
            a=-heapq.heappop(heap)
            b=-heapq.heappop(heap)
            if a==b:
                continue
            else:
                heapq.heappush(heap,-abs(a-b))
        if not heap:
            return 0
        return -heapq.heappop(heap)
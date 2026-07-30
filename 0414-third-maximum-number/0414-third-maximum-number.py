import heapq
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        heap = []
        
        for x in set(nums):        # duplicates hata do
            heapq.heappush(heap, x)
            if len(heap) > 3:
                heapq.heappop(heap)
        if len(heap) == 3:
            return heap[0]
        return max(heap)
import heapq
class pair:
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def __lt__(self,other):
        if self.first!=other.first:
            return self.first < other.first
        return self.second < other.second
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash={}
        for i in nums:
            hash[i]=hash.get(i,0)+1
        heap=[]
        for ele,freq in hash.items():
            curr = pair(freq,ele)
            if len(heap)<k:
                heapq.heappush(heap, curr)
                continue
            if curr.first < heap[0].first:
                continue
            heapq.heappop(heap)
            heapq.heappush(heap, curr)

        ans=[]
        while heap:
            ans.append(heapq.heappop(heap).second)
        return ans
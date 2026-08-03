import heapq
class pair:
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def __lt__(self,other):
        if self.first!=other.first:
            return self.first < other.first
        return self.second > other.second
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hash={}
        for w in words:
            hash[w]=hash.get(w,0)+1
        heap=[]
        for w, freq in hash.items():
            curr = pair(freq, w)
            if len(heap)<k:
                heapq.heappush(heap,curr)
                continue
            if curr.first < heap[0].first:
                continue
            if curr.first == heap[0].first and curr.second > heap[0].second:
                continue
            heapq.heappop(heap)
            heapq.heappush(heap,curr)
        ans=[]
        while heap:
            ans.append(heapq.heappop(heap).second)
        return ans[::-1]

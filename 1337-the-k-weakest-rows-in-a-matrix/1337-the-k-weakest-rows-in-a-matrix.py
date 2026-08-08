class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap=[]
        m=len(mat)
        n=len(mat[0])
        hash={}
        # for i in range(m):
        #     if i not in hash:
        #         hash[i]=mat[i].count(1)
        # for row, ones in hash.items():
        #     curr = (-ones, -row)
               
                    #OR
                    
        for row in range(len(mat)):
            ones = mat[row].count(1)
            curr = (-ones, -row)
            if len(heap)<k:
                heapq.heappush(heap,curr)
            elif curr > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,curr)
        ans=[]
        while heap:
            ans.append(-heapq.heappop(heap)[1])
        return ans[::-1]
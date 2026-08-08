# class node:
    # def __init__(self,val,row,col):
    #     self.val=val
    #     self.row=row
    #     self.col=col
    # def __lt__(self,other):
    #     return self.val>other.val
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m=len(matrix)
        n=len(matrix[0])
        heap=[]
        for row in range(m):
            # curr = node(matrix[row][0],row,0)
            heapq.heappush(heap,(matrix[row][0],row,0))
        ans=[]
        while heap:
            val,row,col = heapq.heappop(heap)
            ans.append(val)
            if col<n-1:
                heapq.heappush(heap,(matrix[row][col+1],row,col+1))
        return ans[k-1]
        
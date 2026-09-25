import heapq
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        i,j = len(grid),len(grid[0])
        if grid[0][0]==1 or grid[i-1][j-1]==1:
            return -1


        dis = [[float('inf')]*j for _ in range(i)]

        heap=[(0,0,0)]
        dis[0][0]=0
        while heap:
            d,r,c=heapq.heappop(heap)
            
            
            if d>dis[r][c]:
                continue
            for dx,dy in ((-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)):
                nr = r+dx
                nc = c+dy
                if nr>=0 and nr<i and nc>=0 and nc<j and grid[nr][nc]==0:
                    if d+1 < dis[nr][nc]:
                        dis[nr][nc]=d+1
                        heapq.heappush(heap,(d+1,nr,nc))

        return -1 if dis[i-1][j-1]==float('inf') else dis[i-1][j-1]+1
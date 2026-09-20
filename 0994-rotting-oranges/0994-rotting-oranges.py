class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        q = deque()
        fresh=0
        time=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    q.append((i,j))
                if grid[i][j]==1:
                    fresh+=1
        
        while q and fresh>0:
            time+=1
            rotten = len(q)
            while(rotten):
                i,j = q.popleft()
                for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
                    nr = dx+i
                    nc = dy+j

                    if nr>=0 and nr<row and nc>=0 and nc<col and grid[nr][nc]==1:
                        q.append((nr,nc))
                        fresh-=1
                        grid[nr][nc]=-1
                rotten-=1
        
        if fresh>0:
            return -1
        return time
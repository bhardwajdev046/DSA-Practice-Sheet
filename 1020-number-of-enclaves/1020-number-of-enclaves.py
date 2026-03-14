class Solution:
    def dfs(self,r,c,visited,grid):
        if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]):
            return
        if visited[r][c]==1:
            return 
        if grid[r][c]==0:
            return 
        visited[r][c]=1
        for dx,dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            self.dfs(r+dx,c+dy,visited,grid)
        return visited
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        visited=[[0]*(col) for _ in range(row)]
        for r in range(row):
            if grid[r][0]==1:
                self.dfs(r,0,visited,grid)
            if grid[r][col-1]==1:
                self.dfs(r,col-1,visited,grid)
        
        for c in range(col):
            if grid[0][c]==1:
                self.dfs(0,c,visited,grid)
            if grid[row-1][c]==1:
                self.dfs(row-1,c,visited,grid)
        count=0
        for r in range(row):
            for c in range(col):
                if visited[r][c]==0 and grid[r][c]==1:
                    count+=1
        return count
        
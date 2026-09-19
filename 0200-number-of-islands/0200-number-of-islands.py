class Solution:
    def bfs(self,i,j,grid,visited):
        q = deque()
        q.append((i,j))
        visited[i][j]=1
        while q:
            r,c = q.popleft()
            for xz,yz in((0,-1),(0,1),(-1,0),(1,0)):
                new_x = r+xz
                new_y = c+yz
                if new_x<0 or new_x>=len(grid) or new_y<0 or new_y>=len(grid[0]):
                    continue
                if visited[new_x][new_y]==1:
                    continue
                if grid[new_x][new_y]=='0':
                    continue
                q.append((new_x,new_y))
                visited[new_x][new_y]=1

    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0]*cols for _ in range(rows)]
        count=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1' and visited[i][j]==0:
                    count+=1
                    self.bfs(i,j,grid,visited)
        return count
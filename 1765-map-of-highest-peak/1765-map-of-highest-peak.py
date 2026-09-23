class Solution:
    def highestPeak(self, isWater: list[list[int]]) -> list[list[int]]:
        row = len(isWater)
        col = len(isWater[0])
        q=deque()

        res = [[-1]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if isWater[i][j]==1:
                    res[i][j]=0
                    q.append((i,j))

        while q:
            r,c = q.popleft()
            for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
                nr = r+dx
                nc = c+dy

                if nr>=0 and nr<row and nc>=0 and nc<col and res[nr][nc]==-1:
                    res[nr][nc] = res[r][c]+1
                    q.append((nr,nc))
        return res
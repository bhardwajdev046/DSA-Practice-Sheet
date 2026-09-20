class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        row = len(mat)
        col = len(mat[0])
        res=[[-1]*col for _ in range(row)]
        q=deque()


            

        for i in range(row):
            for j in range(col):
                if mat[i][j]==0:
                    res[i][j]=0
                    q.append((i,j))
        while q:
            r,c = q.popleft()
            for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
                nr=r+dx
                nc=c+dy
                if nr>=0 and nr<row and nc>=0 and nc<col and res[nr][nc]==-1:
                    res[nr][nc]=res[r][c]+1
                    q.append((nr,nc))

        return res
        
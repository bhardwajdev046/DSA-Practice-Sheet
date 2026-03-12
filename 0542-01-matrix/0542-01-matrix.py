from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row=len(mat)
        col=len(mat[0])
        visited=[[0]*(col) for _ in range(row)]
        distance=[[0]*(col) for _ in range(row)]
        queue=deque()
        for r in range(row):
            for c in range(col):
                if mat[r][c]==0:
                    queue.append([r,c,0])
                    visited[r][c]=1
        while queue:
            i,j,d=queue.popleft()
            distance[i][j]=d
            for dx,dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                new_r,new_c=(i+dx),(j+dy)
                if new_r<0 or new_c<0 or new_r>=row or new_c>=col:
                    continue
                if visited[new_r][new_c]!=1:
                    queue.append([new_r,new_c,d+1])
                    visited[new_r][new_c]=1
        return distance

        
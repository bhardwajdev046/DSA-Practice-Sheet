from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        new_grid=deepcopy(grid)
        fresh=0
        queue=deque()
        for r in range(row):
            for c in range(col):
                if new_grid[r][c]==2:
                    queue.append((r,c))
                elif new_grid[r][c]==1:
                    fresh+=1
        minutes=0
        while queue and fresh>0:
            minutes+=1
            rotten=len(queue)
            for _ in range(rotten):
                r,c=queue.popleft()
                for dx,dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    new_r , new_c = dx+r, dy+c
                    if new_r<0 or new_r==row or new_c<0 or new_c==col:
                        continue
                    if new_grid[new_r][new_c]==0 or new_grid[new_r][new_c]==2:
                        continue
                    fresh-=1
                    queue.append((new_r,new_c))
                    new_grid[new_r][new_c]=2
        if fresh>0:
            return -1
        else:
            return minutes
            
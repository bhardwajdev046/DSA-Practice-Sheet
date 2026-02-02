class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        def fun(i,j1,j2,grid,dp):
            if j1<0 or j1>=len(grid[0]) or j2<0 or j2>=len(grid[0]):
                return float('-inf')
            if i==len(grid)-1:
                if j1==j2:
                    return grid[i][j1]
                else:
                    return grid[i][j1]+grid[i][j2]
            if dp[i][j1][j2]!=-1:
                return dp[i][j1][j2]
            maxi=0
            for r1 in range(-1,2):
                for r2 in range(-1,2):
                    if j1==j2:
                        maxi=max(maxi,grid[i][j1]+fun(i+1,j1+r1,j2+r2,grid,dp))
                    else:
                        maxi=max(maxi,grid[i][j1]+grid[i][j2]+fun(i+1,j1+r1,j2+r2,grid,dp))
            dp[i][j1][j2]=maxi
            return dp[i][j1][j2]

        row=len(grid)
        col=len(grid[0])
        dp = [[[-1]*col for _ in range(col)] for _ in range(row)]
        return fun(0,0,col-1,grid,dp)
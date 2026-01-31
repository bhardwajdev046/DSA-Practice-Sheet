class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # def fun(i,j,grid,dp):
        #     if i<0 or j<0:
        #         return float('inf')
        #     if i==0 and j==0:
        #         return grid[i][j]
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
        #     left= grid[i][j] + fun(i,j-1,grid,dp)
        #     up= grid[i][j] + fun(i-1,j,grid,dp)
        #     dp[i][j]= min(left,up)
        #     return dp[i][j]
        # i=len(grid)
        # j=len(grid[0])
        # dp=[[-1]*j for i in range(i)]
        # return fun(i-1,j-1,grid,dp)
        def fun(m,n,grid):
            dp=[[-1]*n for i in range(m)]
            dp[0][0]=grid[0][0]
            
            for i in range(m):
                for j in range(n):
                    if i==0 and j==0:
                        continue
                    left= dp[i][j-1] if j>0 else float('inf')
                    up= dp[i-1][j] if i>0 else float('inf')
                    dp[i][j]=grid[i][j]+min(left,up)
            return dp[m-1][n-1]
        mp=len(grid)
        np=len(grid[0])
        return fun(mp,np,grid)
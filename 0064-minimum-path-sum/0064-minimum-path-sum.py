class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def fun(i,j,grid,dp):
            if i<0 or j<0:
                return float('inf')
            if i==0 and j==0:
                return grid[i][j]
            if dp[i][j]!=-1:
                return dp[i][j]
            left= grid[i][j] + fun(i,j-1,grid,dp)
            up= grid[i][j] + fun(i-1,j,grid,dp)
            dp[i][j]= min(left,up)
            return dp[i][j]
        i=len(grid)
        j=len(grid[0])
        dp=[[-1]*j for i in range(i)]
        return fun(i-1,j-1,grid,dp)
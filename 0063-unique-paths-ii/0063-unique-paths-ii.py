class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def fun(i,j,obstacleGrid,dp):
            if obstacleGrid[i][j]==1:
                return 0
            if i==0 and j==0:
                return 1
            if i<0 or j<0:
                return 0
            
            if dp[i][j]!=-1:
                return dp[i][j]
            left=fun(i,j-1,obstacleGrid,dp)
            up=fun(i-1,j,obstacleGrid,dp)
            dp[i][j]=left+up
            return dp[i][j]
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[-1]*n for _ in range(m)]
        return fun(m-1,n-1,obstacleGrid,dp)
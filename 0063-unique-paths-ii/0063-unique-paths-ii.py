class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # def fun(i,j,obstacleGrid,dp):
        #     if i<0 or j<0:
        #         return 0
        #     if obstacleGrid[i][j]==1:
        #         return 0
        #     if i==0 and j==0:
        #         return 1
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
        #     left=fun(i,j-1,obstacleGrid,dp)
        #     up=fun(i-1,j,obstacleGrid,dp)
        #     dp[i][j]=left+up
        #     return dp[i][j]
        # i=len(obstacleGrid)
        # j=len(obstacleGrid[0])
        # dp=[[-1]*j for _ in range(i)]
        # return fun(i-1,j-1,obstacleGrid,dp)

        def fun(row,col,obstacleGrid):
            if obstacleGrid[0][0] == 1:
                return 0
            dp=[[-1]*col for _ in range(row)]
            dp[0][0]=1
            for i in range(row):
                for j in range(col):
                    if i==0 and j==0:
                        continue
                    if obstacleGrid[i][j]==1:
                        dp[i][j]=0
                        continue
                    left=dp[i][j-1] if j>0 else 0
                    up=dp[i-1][j] if i>0 else 0
                    dp[i][j]=left+up
            return dp[row-1][col-1]
        i=len(obstacleGrid)
        j=len(obstacleGrid[0])
        return fun(i,j,obstacleGrid)
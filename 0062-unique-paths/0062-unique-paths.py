class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*(n+1) for i in range(m+1)]
        dp[1][1]=1
        for i in range(m+1):
            for j in range(n+1):
                if i==1 and j==1:
                    continue
                if j>1:
                    left=dp[i][j-1]
                else:
                    left=0
                if i>1:
                    up=dp[i-1][j]
                else:
                    up=0
                dp[i][j]=left+up
        return dp[m][n]
        
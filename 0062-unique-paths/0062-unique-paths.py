class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def fun(i,j,dp):
            if i==1 and j==1:
                return 1
            if i<1 or j<1:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            left=fun(i,j-1,dp)
            up=fun(i-1,j,dp)
            dp[i][j]=left+up
            return dp[i][j]

        dp=[[-1]*(n+1) for i in range(m+1)]
        return (fun(m,n,dp))
        
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        def fun(m,n):
            dp=[[0]*(n+1) for _ in range(m+1)]
            for i in range(1,m+1):
                for j in range(1,n+1):
                    if word1[i-1]==word2[j-1]:
                        dp[i][j]=1+dp[i-1][j-1]
                    else:
                        dp[i][j]=max(dp[i-1][j],dp[i][j-1])
            return dp[m][n]
        temp=fun(m,n)
        return (m-temp)+(n-temp)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m=len(s)
        n=len(t)
        dp=[[-1]*(n) for _ in range(m)]
        def fun(i,j):
            if j<0:
                return 1
            if i<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if s[i]==t[j]:
                pick=fun(i-1,j-1)
                skip=fun(i-1, j)
                dp[i][j]=(pick+skip)
                return dp[i][j]
            else:
                dp[i][j]=fun(i-1,j)
                return dp[i][j]
        return fun(m-1,n-1)
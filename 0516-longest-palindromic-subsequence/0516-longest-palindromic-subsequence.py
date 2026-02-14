class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # m=len(s)
        # def fun(i,j):
        #     if i>j:
        #         return 0
        #     if i==j:
        #         return 1
        #     if s[i]==s[j]:
        #         return 2+fun(i+1,j-1)
        #     else:
        #         return max(fun(i+1,j),fun(i,j-1))
        # return fun(0,m-1)

        s2=s[::-1]
        def fun(m,n):
            dp=[[0]*(n+1) for _ in range(m+1)]
            for i in range(1,m+1):
                for j in range(1,n+1):
                    if s[i-1]==s2[j-1]:
                        dp[i][j]=1+dp[i-1][j-1]
                    else:
                        dp[i][j]=max(dp[i-1][j],dp[i][j-1])
            return dp[m][n]
        return fun(len(s),len(s2))
                
        
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        # cost = [[0] * (n + 1) for _ in range(m + 1)]
        # for i in range(1,m+1):
        #     cost[i][0]=i
        # for j in range(1,n+1):
        #     cost[0][j]=j 
        # for i in range(1,m+1):
        #     for j in range(1,n+1):
        #         if word2[i-1]==word1[j-1]:
        #             cost[i][j]=cost[i-1][j-1]
        #         else:
        #             topleft=cost[i-1][j-1]
        #             top=cost[i-1][j]
        #             left=cost[i][j-1]
        #             cost[i][j]=1+min(top,left,topleft)
        # return cost[m][n]
        dp=[[-1]*m for _ in range(n)]
        def fun(i,j):
            if i<0:
                return j+1
            if j<0:
                return i+1
            if dp[i][j]!=-1:
                return dp[i][j]
            if word1[i]==word2[j]:
                dp[i][j]=0+fun(i-1,j-1)
                return dp[i][j]
            else:
                dp[i][j]=min(1+fun(i,j-1), 1+fun(i-1,j), 1+fun(i-1,j-1)) 
                return dp[i][j]
        return fun(n-1,m-1)
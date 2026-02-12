class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        idx1=len(text1)
        idx2=len(text2)
        # dp=[[-1]*(idx2) for _ in range(idx1)]
        # def fun(idx1,idx2,dp):
        #     if idx1<0 or idx2<0:
        #         return 0
        #     if dp[idx1][idx2]!=-1:
        #         return dp[idx1][idx2]
        #     if text1[idx1]==text2[idx2]:
        #         dp[idx1][idx2]= 1+fun(idx1-1,idx2-1,dp)
        #         return dp[idx1][idx2]
        #     else:
        #         dp[idx1][idx2]= max(fun(idx1,idx2-1,dp),fun(idx1-1,idx2,dp))
        #         return dp[idx1][idx2]

        def fun(idx1,idx2):
            dp=[[0]*(idx2+1) for _ in range(idx1+1)]
       
            for i in range(1,idx1+1):
                for j in range(1,idx2+1):
                    if text1[i-1]==text2[j-1]:
                        dp[i][j]= 1+dp[i-1][j-1]
                    else:
                        dp[i][j]= max(dp[i][j-1],dp[i-1][j])
            return dp[idx1][idx2]
        return fun(idx1,idx2)
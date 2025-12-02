class Solution:
    def climbStairs(self, n: int) -> int:
        # def fun(n,dp):
        #     if n<=1:                   
        #         return 1
        #     if dp[n]!=-1:                       #MEMORIZATION
        #         return dp[n]
        #     dp[n]=fun(n-1,dp)+fun(n-2,dp)
        #     return dp[n]
        # dp=[-1]*(n+1) 
        # return fun(n,dp)

        # if n<=1:
        #     return 1
        # dp=[-1]*(n+1)
        # dp[0]=1                                  #TABULATION
        # dp[1]=1
        # for idx in range(2,n+1):
        #     dp[idx]=dp[idx-1]+dp[idx-2]
        # return dp[n]

        if n<=1:
            return 1
        prev=1                                  #TABULATION OPTIMIZE
        prev1=1
        for idx in range(2,n+1):
            curr=prev+prev1
            prev=prev1
            prev1=curr
        return prev1
        
        
class Solution:
    def fib(self, n: int) -> int:
        # def fun(n):
        #     if n==0:
        #         return 0
        #     if n==1:
        #         return 1
        #     return fun(n-1)+fun(n-2)
        # return fun(n)

        # def fun(n,dp):
        #     if n==0:
        #         return 0
        #     if n==1:
        #         return 1                            #MEMORIZATION (top-down)approach
        #     if dp[n]!=-1:
        #         return dp[n]
        #     dp[n] = fun(n-1,dp)+fun(n-2,dp)
        #     return dp[n]
        # dp=[-1]*(n+1)    
        # return fun(n,dp)
        
        # def fun(n):
        #     if n <= 1:
        #         return n
        #     dp=[-1]*(n+1)
        #     dp[0]=0
        #     dp[1]=1                            #TABULATION (bottom-up)approach
        #     for idx in range(2,n+1):
        #         dp[idx] = dp[idx-1]+dp[idx-2]
        #     return dp[n]    
        # return fun(n)

        def fun(n):
            if n <= 1:
                return n
            dp=[-1]*(n+1)
            prev=0
            prev1=1                        #TABULATION-OPTIMIZE (bottom-up)approach
            for idx in range(2,n+1):
                curr = prev+prev1
                prev=prev1
                prev1=curr
            return prev1   
        return fun(n)
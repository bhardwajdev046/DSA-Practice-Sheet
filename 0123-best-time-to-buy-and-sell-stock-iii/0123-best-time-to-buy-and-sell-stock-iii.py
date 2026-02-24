class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[[-1]*3 for _ in range(2)] for i in range(n)]
        def fun(i,buy,limit):
            if i==n:
                return 0
            if limit==0:
                return 0
            if dp[i][buy][limit]!=-1:
                return dp[i][buy][limit]
            if buy==1:
                profit=max(-prices[i]+fun(i+1,0,limit),
                            0+fun(i+1,1,limit))
            else:
                profit=max(prices[i]+fun(i+1,1,limit-1),
                            0+fun(i+1,0,limit))
            dp[i][buy][limit]=profit
            return dp[i][buy][limit]
        return fun(0,1,2)
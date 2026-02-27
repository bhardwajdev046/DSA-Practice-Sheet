class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)
        dp=[[-1]*2 for _ in range(n)]
        def fun(i,buy):
            if i==n:
                return 0
            if dp[i][buy]!=-1:
                return dp[i][buy]
            if buy==1:
                profit=max(-prices[i]+fun(i+1,0),0+fun(i+1,1))
            else:
                profit=max(prices[i]+fun(i+1,1)-fee,0+fun(i+1,0))
            dp[i][buy]=profit
            return dp[i][buy]
        return fun(0,1)

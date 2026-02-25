class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # n=len(prices)
        # def fun(idx,buy,limit):
        #     ahead=[[0]*(limit+1) for _ in range(buy+1)]
        #     curr=[[0]*(limit+1) for _ in range(buy+1)]
        #     for i in range(n-1,-1,-1):
        #         for b in range(buy+1):
        #             for lim in range(1,limit+1):
        #                 if b==1:
        #                     profit=max(-prices[i]+ahead[0][lim],
        #                                 0+ahead[1][lim])
        #                 else:
        #                     profit=max(prices[i]+ahead[1][lim-1],
        #                                 0+ahead[0][lim])

        #                 curr[b][lim]=profit
        #         ahead=curr
        #     return curr[buy][limit]
        # return fun(0,1,k)

        n=len(prices)
        dp=[[[-1]*(k+1) for _ in range(2)]for _ in range(n)]
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
        return fun(0,1,k)
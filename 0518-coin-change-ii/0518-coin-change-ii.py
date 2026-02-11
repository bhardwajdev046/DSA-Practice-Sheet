class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        # dp=[[-1]*(amount+1) for _ in range(n)]
        # def fun(i,amount):
        #     if i==0:
        #         if amount%coins[0]==0:
        #             return 1
        #         return 0
        #     if dp[i][amount]!=-1:
        #         return dp[i][amount]
        #     pick=0                    
        #     if amount>=coins[i]:
        #         pick=fun(i,amount-coins[i])
        #     notpick=fun(i-1,amount)
        #     dp[i][amount]=pick+notpick
        #     return dp[i][amount]

        # def fun(idx,amount):
        #     dp=[[-1]*(amount+1) for _ in range(n)]
        #     for i in range(amount+1):
        #         if i%coins[0]==0:
        #             dp[0][i]=1
        #         else:
        #             dp[0][i]=0
        #     for i in range(1,idx+1):
        #         for amt in range(amount+1):
        #             pick=0                    
        #             if amt>=coins[i]:
        #                 pick=dp[i][amt-coins[i]]
        #             notpick=dp[i-1][amt]
        #             dp[i][amt]=pick+notpick
        #     return dp[idx][amount]

        def fun(idx,amount):
            prev=[0]*(amount+1)
            for i in range(amount+1):
                if i%coins[0]==0:
                    prev[i]=1

            for i in range(1,idx+1):
                curr=[0]*(amount+1)
                for amt in range(amount+1):
                    pick=0                    
                    if amt>=coins[i]:
                        pick=curr[amt-coins[i]]
                    notpick=prev[amt]
                    curr[amt]=pick+notpick
                prev=curr
            return prev[amount]

    
        return fun(n-1,amount)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        dp=[[-1]*(amount+1) for _ in range(n)]
        def fun(i,amount):
            if i==0:
                if amount%coins[0]==0:
                    return 1
                return 0
            if dp[i][amount]!=-1:
                return dp[i][amount]
            pick=0
            if amount>=coins[i]:
                pick=fun(i,amount-coins[i])
            notpick=fun(i-1,amount)
            dp[i][amount]=pick+notpick
            return dp[i][amount]
    
        return fun(n-1,amount)
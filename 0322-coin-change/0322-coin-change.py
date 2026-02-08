class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def fun(idx,coins,amount,dp):
            if amount==0:
                return 0
            if idx<0 or amount<0:
                return float('inf')
            if dp[idx][amount]!=-1:
                return dp[idx][amount]
            pick= fun(idx,coins,amount-coins[idx],dp)
            notpick=fun(idx-1,coins,amount,dp)
            dp[idx][amount]= min(1+pick,notpick)
            return dp[idx][amount]

        idx=len(coins)-1
        dp=[[-1]*(amount+1) for _ in range(idx+1)]
        if fun(idx,coins,amount,dp)==float('inf'):
            return -1
        else:
            return fun(idx,coins,amount,dp)

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
        
#         def fun(idx, amount):
#             if amount == 0:
#                 return 0
#             if idx < 0 or amount < 0:
#                 return float('inf') 
#             if dp[idx][amount] != -1:
#                 return dp[idx][amount]
#             pick = fun(idx, amount - coins[idx])
#             notpick = fun(idx - 1, amount)         
#             dp[idx][amount] = min(1 + pick, notpick)
#             return dp[idx][amount]
        
#         n = len(coins)
#         dp = [[-1] * (amount + 1) for _ in range(n)]
#         ans = fun(n - 1, amount)
#         return -1 if ans == float('inf') else ans

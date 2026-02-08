class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # def fun(idx,coins,amount,dp):
        #     if amount==0:
        #         return 0
        #     if idx<0 or amount<0:
        #         return float('inf')
        #     if dp[idx][amount]!=-1:
        #         return dp[idx][amount]
        #     pick= fun(idx,coins,amount-coins[idx],dp)
        #     notpick=fun(idx-1,coins,amount,dp)
        #     dp[idx][amount]= min(1+pick,notpick)
        #     return dp[idx][amount]

        # idx=len(coins)-1
        # dp=[[-1]*(amount+1) for _ in range(idx+1)]
        # if fun(idx,coins,amount,dp)==float('inf'):
        #     return -1
        # else:
        #     return fun(idx,coins,amount,dp)

        
        def fun(idx, amount):
            dp = [[-1] * (amount + 1) for _ in range(n)]
            for i in range(idx+1):
                dp[i][0]=0
            for amt in range(amount+1):
                if amt%coins[0]==0:
                    dp[0][amt]=amt//coins[0]
                else:
                    dp[0][amt]=float('inf')
            
            for i in range(1,idx+1):
                for amt in range(1,amount+1):
                    pick=float('inf')
                    if amt >= coins[i]:
                        pick = dp[i][amt - coins[i]]
                    notpick = dp[i-1][amt]         
                    dp[i][amt] = min(1 + pick, notpick)
            return dp[idx][amount]
        
        n = len(coins)
        ans = fun(n - 1, amount)
        return -1 if ans == float('inf') else ans

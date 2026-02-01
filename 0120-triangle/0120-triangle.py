class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # def fun(m,n,ar,dp):
        #     if m==a-1:
        #         return ar[m][n]
        #     if dp[m][n]!=-1:
        #         return dp[m][n]
    
        #     down=ar[m][n]+fun(m+1,n,ar,dp)
        #     right=ar[m][n]+fun(m+1,n+1,ar,dp)
        #     dp[m][n]= min(down,right)
        #     return dp[m][n] 
        # a=len(triangle)
        # b=len(triangle[a-1])
        # dp=[[-1]*b for _ in range(a)]
        # return fun(0,0,triangle,dp)

        def fun(m,n,ar):
            a=len(ar)
            b=len(ar[a-1])
            dp=[[-1]*b for _ in range(a)]
            for k in range(b):
                dp[a-1][k]=ar[a-1][k]

            for i in range(a-2,-1,-1):
                for j in range(i,-1,-1):
                    down=dp[i+1][j] if i<a-1 else float('inf')
                    right=dp[i+1][j+1] if (i<a-1 and j<b) else float('inf')
                    dp[i][j]=ar[i][j]+min(down,right)
            return dp[0][0] 
        return fun(0,0,triangle)
        
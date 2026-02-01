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

        # def fun(m,n,ar):
        #     row=len(ar)
        #     col=len(ar[row-1])
        #     dp=[[-1]*col for _ in range(row)]
        #     for k in range(col):
        #         dp[row-1][k]=ar[row-1][k]

        #     for i in range(row-2,-1,-1):
        #         for j in range(i,-1,-1):
        #             down=dp[i+1][j] if i<row-1 else float('inf')
        #             right=dp[i+1][j+1] if (i<row-1 and j<col) else float('inf')
        #             dp[i][j]=ar[i][j]+min(down,right)
        #     return dp[0][0] 
        # return fun(0,0,triangle)

        def fun(m,n,ar):
            row=len(ar)
            col=len(ar[row-1])
            prev=[0]*col
            for k in range(col):
                prev[k]=ar[row-1][k]

            for i in range(row-2,-1,-1):
                curr=[0]*(i+1)
                for j in range(0,i+1):
                    down=prev[j] 
                    right=prev[j+1]
                    curr[j]=ar[i][j]+min(down,right)
                prev=curr
            return prev[m] 
        return fun(0,0,triangle)
        
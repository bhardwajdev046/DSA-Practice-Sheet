class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # def fun(row,col,matrix,dp):
        #     if col<0 or col>=len(matrix):
        #         return float('inf')
        #     if row==0:
        #         return matrix[0][col]
        #     if dp[row][col]!=-1:
        #         return dp[row][col]
        #     up=matrix[row][col] + fun(row-1,col,matrix,dp)
        #     ld=matrix[row][col] + fun(row-1,col-1,matrix,dp)
        #     rd=matrix[row][col] + fun(row-1,col+1,matrix,dp)
        #     dp[row][col]= min(up,ld,rd)
        #     return dp[row][col]
        # row=len(matrix)
        # col=len(matrix[0])
        # mini=float('inf')
        # dp=[[-1]*row for _ in range(col)]
        # for k in range(col):
        #     mini=min(mini,fun(row-1,k,matrix,dp))
        # return mini
        
        row=len(matrix)
        col=len(matrix[0])
        dp=[[None]*col for _ in range(row)]
        for k in range(col):
            dp[0][k]=matrix[0][k]

        for i in range(1,row):
            for j in range(col):
                up=matrix[i][j] + dp[i-1][j] if i>0 else float('inf')
                ld=matrix[i][j] + dp[i-1][j-1] if (i>0 and j>0) else float('inf') 
                rd=matrix[i][j] + dp[i-1][j+1] if (i>0 and j<col-1) else float('inf')
                dp[i][j]= min(up,ld,rd)

        mini=float('inf')
        for k in range(col):
            mini=min(mini,dp[row-1][k])
        return mini
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
        # dp=[[-1]*col for _ in range(row)]
        # for k in range(col):
        #     mini=min(mini,fun(row-1,k,matrix,dp))
        # return mini
        
        row=len(matrix)
        col=len(matrix[0])
        prev=[0]*col
        for k in range(col):
            prev[k]=matrix[0][k]

        for i in range(1,row):
            curr=[0]*col
            for j in range(col):
                up=matrix[i][j] + prev[j] if i>0 else float('inf')
                ld=matrix[i][j] + prev[j-1] if j>0 else float('inf') 
                rd=matrix[i][j] + prev[j+1] if j<col-1 else float('inf')
                curr[j]= min(up,ld,rd)
            prev=curr
        mini=float('inf')
        for k in range(col):
            mini=min(mini,prev[k])
        return mini
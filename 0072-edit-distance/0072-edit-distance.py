class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        cost = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1,m+1):
            cost[i][0]=i
        for j in range(1,n+1):
            cost[0][j]=j 
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word2[i-1]==word1[j-1]:
                    cost[i][j]=cost[i-1][j-1]
                else:
                    topleft=cost[i-1][j-1]
                    top=cost[i-1][j]
                    left=cost[i][j-1]
                    cost[i][j]=1+min(top,left,topleft)

        return cost[m][n]
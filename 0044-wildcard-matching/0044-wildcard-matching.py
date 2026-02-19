class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m=len(s)
        n=len(p)
        dp=[[-1]*n for _ in range(m)]
        def fun(s,p,i,j):
            if i<0 and j<0:
                return True
            if i>=0 and j<0:
                return False
            if i<0 and j>=0:
                for x in range(j+1):
                    if p[x]!="*":
                        return False
                return True
            if dp[i][j]!=-1:
                return dp[i][j]
            if s[i]==p[j] or p[j]=="?":
                dp[i][j] = fun(s,p,i-1,j-1)
            elif p[j]=="*":
                dp[i][j] = fun(s,p,i-1,j) or fun(s,p,i,j-1)
            else:
                dp[i][j]=False
            return dp[i][j]
        return fun(s,p,m-1,n-1)
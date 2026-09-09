class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = len(s)
        j = len(p)
        dp=[[-1]*(j+1) for _ in range(i+1)]
        def fun(i,j,s,p):
            if j==0:
                return i==0

            if dp[i][j]!=-1:
                return dp[i][j]

            if p[j-1]=='*':
                not_take = fun(i,j-2,s,p)
                first_match = False
                if i>0 and (p[j-2]==s[i-1] or p[j-2]=='.'):
                    first_match =True
            
                take = first_match and fun(i-1,j,s,p)
                dp[i][j]= take or not_take
                return dp[i][j]
            else:
                first_match = False

                if i > 0 and (p[j-1] == s[i-1] or p[j-1] == '.'):
                    first_match = True
                dp[i][j]=first_match and fun(i-1,j-1,s,p) if i>0 else False
                return dp[i][j]
        return fun(i,j,s,p)
        
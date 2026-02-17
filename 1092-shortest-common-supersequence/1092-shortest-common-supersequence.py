class Solution:
    def fun(self,str1,str2,m,n):
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        i,j=m,n
        res=[]
        while i>0 and j>0:
            if str1[i-1]==str2[j-1]:
                res.append(str1[i-1])
                i-=1
                j-=1
            else:
                if dp[i-1][j]>=dp[i][j-1]:
                    i-=1
                else:
                    j-=1
        return ''.join(reversed(res))
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m=len(str1)
        n=len(str2)
        lcs=self.fun(str1,str2,m,n)
        i,j=0,0
        ans=""
        for ch in lcs:
            while i<m and str1[i]!=ch:
                ans+=str1[i]
                i+=1
            while j<n and str2[j]!=ch:
                ans+=str2[j]
                j+=1
            ans+=ch
            i+=1
            j+=1
        ans+=str1[i:]
        ans+=str2[j:]
        return ans
        
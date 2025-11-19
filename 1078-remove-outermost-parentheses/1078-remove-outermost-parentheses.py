class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=[]
        count=0
        for i in range(len(s)):
            if s[i]=='(':
                count+=1
            else:
                count-=1
            if s[i]=='(' and count>1:
                res.append('(')
            if s[i]==')' and count>0:
                res.append(')')
        return "".join(res)
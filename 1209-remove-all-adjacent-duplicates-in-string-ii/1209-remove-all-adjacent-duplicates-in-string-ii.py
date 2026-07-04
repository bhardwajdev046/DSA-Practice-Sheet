class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        n=len(s)
        for i in range(n):
            count=1
            if stack and stack[-1][0]==s[i]:
                stack[-1][1]+=1
            else:
                stack.append([s[i],1])
            if stack[-1][1]==k:
                stack.pop()
        
        temp=[]
        for ch,freq in stack:
            temp.append(ch*freq)
        return "".join(temp)
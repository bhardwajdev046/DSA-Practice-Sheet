class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:
            return 0
        temp=[]
        add=0
        for i in str(n):
            if i!='0':
                temp.append(i)
                add+=int(i)
        k="".join(temp)
        return int(k)*add
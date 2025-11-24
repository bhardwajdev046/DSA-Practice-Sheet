class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(char,i,j):
            while i<j:
                char[i],char[j] = char[j],char[i]
                i+=1
                j-=1
            return "".join(char)
            # res=""
            # for i in string[::-1]:
            #     res+=i
            # return res

        i=0
        char=list(s)
        n=len(char)
        for j in range(n+1):
            if j==n or char[j]==" ":
                reverse(char,i,j-1)
                i=j+1
        return "".join(char)
        
        
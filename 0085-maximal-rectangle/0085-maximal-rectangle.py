class Solution:
    def rectangle(self,arr):
        stack=[]
        ans=0
        n=len(arr)
        for i in range(n):
            while stack and arr[stack[-1]]>arr[i]:
                index=stack.pop()
                if stack:
                    ans=max(ans, arr[index]*(i-stack[-1]-1))
                else:
                    ans=max(ans, arr[index]*(i))
            stack.append(i)
        while stack:
            index=stack.pop()
            if stack:
                ans=max(ans, arr[index]*(n-stack[-1]-1))
            else:
                ans=max(ans, arr[index]*(n))
        return ans

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        row=len(matrix)
        col=len(matrix[0])
        height=[0]*(col)
        res=0
        for i in range(row):
            for j in range(col):
                if matrix[i][j]=='0':
                    height[j]=0
                else:
                    height[j]+=1
            res=max(res, self.rectangle(height))
        return res
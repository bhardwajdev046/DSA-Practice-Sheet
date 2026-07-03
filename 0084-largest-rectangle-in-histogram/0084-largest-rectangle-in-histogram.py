class Solution:
    def prevsmaller(self, arr):
        res=[]
        res.append(-1)
        stack=[]
        stack.append(0)
        for i in range(1,len(arr)):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if not stack:
                res.append(-1)
            else:
                res.append(stack[-1])
            stack.append(i)
        return res
    def nextsmaller(self, arr):
        res2=[]
        res2.append(len(arr))
        stack=[]
        stack.append(len(arr)-1)
        for i in range(len(arr)-2,-1,-1):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if not stack:
                res2.append(len(arr))
            else:
                res2.append(stack[-1])
            stack.append(i)
        return res2[::-1]
    def largestRectangleArea(self, heights: List[int]) -> int:
        ps=self.prevsmaller(heights)
        ns=self.nextsmaller(heights)

        res=0
        maxi=0
        for i in range(len(heights)):
            res  = heights[i]*(ns[i]-ps[i]-1)
            maxi=max(maxi,res)
        return maxi
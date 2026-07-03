class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans=0
        stack=[]
        n=len(heights)
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                index=stack.pop()
                if stack:
                    ans=max(ans, heights[index]*(i-stack[-1]-1))
                else:
                    ans=max(ans, heights[index]*i)
            stack.append(i)
        while stack:
            index=stack.pop()
            if stack:
                ans=max(ans, heights[index]*(n-stack[-1]-1))
            else:
                ans=max(ans, heights[index]*n)
        return ans

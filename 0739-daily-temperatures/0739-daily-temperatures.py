class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[]
        res.append(0)
        stack=[]
        stack.append(len(temperatures)-1)
        
        for i in range(len(temperatures)-2,-1,-1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if not stack:
                res.append(0)
            else:
                res.append(stack[-1]-i)
            stack.append(i)
        return res[::-1]
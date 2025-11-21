class Solution:
    def maxDepth(self, s: str) -> int:
        # count=0
        # maxi=0
        # for i in s:
        #     if i=="(":
        #         count+=1
        #     elif i==")":
        #         count-=1
        #     maxi=max(count,maxi)
        # return maxi
        stack=[]
        max_depth=0
        current_depth=0
        for i in s:
            if i=="(":
                current_depth+=1
                stack.append('(')
            elif i==")":
                current_depth-=1
                stack.pop()
            max_depth=max(current_depth,max_depth)
        return max_depth

# class Solution:
#     def solve(self, index, close_count,open_used, brackets, result, n):
#         if index == len(brackets):
#             result.append("".join(brackets))
#             return
        
#         if open_used < n:
#             brackets[index] = "("
#             self.solve(index + 1, close_count , open_used + 1, brackets, result, n)

#         if close_count < open_used:
#             brackets[index] = ")"
#             self.solve(index + 1, close_count+1 ,open_used, brackets, result, n)

#     def generateParenthesis(self, n: int) -> List[str]:
#         brackets = [""] * (n * 2)
#         result = []
#         self.solve(0, 0, 0, brackets, result, n)
#         return result

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def fun(s1,left,right,n,li):
            if left+right==2*n:
                li.append(s1)
                return li
            
            if left<n:
                fun(s1+"(",left+1,right,n,li)
            
            if left>right:
                fun(s1+")",left,right+1,n,li)

        li=[]
        fun("",0,0,n,li)
        return li
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def fun(up, p, i, n):
            if i==n:
                return [up]

            temp=p[i]
            take = fun(up+[temp], p, i+1, n)
            
            not_take = fun(up, p, i+1, n)

            return take + not_take
        
        return fun([],nums,0,len(nums))
        
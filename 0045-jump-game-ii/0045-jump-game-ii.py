# class Solution:
#     def jump(self, nums: List[int]) -> int:
        # cache={}
        # def helper(i,nums):
        #     if i>=len(nums)-1:
        #         return 0
        #     if i in cache:                # DP Solution
        #         return cache[i]
        #     if nums[i]==0:
        #         return float('inf')
        #     min_steps=float('inf')
        #     for s in range(1,nums[i]+1):
        #         ans=1+helper(i+s,nums)
        #         min_steps=min(min_steps,ans)

        #     cache[i]=min_steps
        #     return min_steps
        # return helper(0,nums)

                     
                                   #GREEDY Solution           
class Solution:
    def jump(self, nums: List[int]) -> int:
        left,right=0,0
        jump=0
        while right<len(nums)-1:
            farthest=0
            for i in range(left,right+1):
                farthest=max(farthest,i+nums[i])
            left=right+1
            right=farthest
            jump+=1
        return jump
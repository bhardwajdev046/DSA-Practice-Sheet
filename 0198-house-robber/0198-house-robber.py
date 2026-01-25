class Solution:
    def rob(self, nums: List[int]) -> int:
        # def fun(idx,nums):
        #     if idx==0:
        #         return nums[0]
        #     if idx<0:
        #         return 0

        #     rob=nums[idx]+fun(idx-2,nums)
        #     skip= 0 + fun(idx-1,nums)

        #     return max(rob,skip)
        
        # idx=len(nums)-1
        # return fun(idx,nums)

        def fun(idx,nums,dp):
            if idx==0:
                return nums[0]
            if idx<0:
                return 0
            if dp[idx]!=-1:
                return dp[idx]

            rob = nums[idx] + fun(idx-2,nums,dp)
            skip = 0 + fun(idx-1,nums,dp)

            dp[idx]=max(rob,skip)
            return dp[idx]
        
        idx=len(nums)-1
        dp=[-1]*(idx+1)
        return fun(idx,nums,dp)
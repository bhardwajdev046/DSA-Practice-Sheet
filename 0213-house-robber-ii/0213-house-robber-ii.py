class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # def fun(idx,nums,dp):
        #     if idx==0:
        #         return nums[0]
        #     if idx<0:
        #         return 0
        #     if dp[idx]!=-1:
        #         return dp[idx]
        #     rob = nums[idx] + fun(idx-2,nums,dp)
        #     skip = 0 + fun(idx-1,nums,dp)

        #     dp[idx]=max(rob, skip)
        #     return dp[idx]
        
        # n=len(nums)
        # dp1=[-1]*(n-1)
        # dp2=[-1]*(n-1)
        # a=fun(n-2,nums[1:],dp1)
        # b=fun(n-2,nums[:-1],dp2)
        # return max(a,b)

        # def fun(idx,nums):
        #     dp=[-1]*(n-1)
        #     dp[0]=nums[0]
        #     for i in range(1,idx+1):
        #         if i>1:
        #             rob = nums[i] + dp[i-2]
        #         else:
        #             rob=nums[i]
        #         skip = 0 + dp[i-1]
        #         dp[i]=max(rob, skip)
        #     return dp[idx]
        
        # n=len(nums)
        # a=fun(n-2,nums[1:])
        # b=fun(n-2,nums[:-1])
        # return max(a,b)

        def fun(idx,nums):
            prev=nums[0]
            prev2=0
            for i in range(1,idx+1):
                if i>1:
                    rob = nums[i] + prev2
                else:
                    rob=nums[i]
                skip = 0 + prev
                current=max(rob, skip)
                prev2=prev
                prev=current
            return prev
        
        n=len(nums)
        a=fun(n-2,nums[1:])
        b=fun(n-2,nums[:-1])
        return max(a,b)
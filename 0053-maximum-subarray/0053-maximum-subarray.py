class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        bestending=res=nums[0]
        for i in range(1,len(nums)):
            c1=bestending+nums[i]
            c2=nums[i]
            bestending=max(c1,c2)
            res=max(res,bestending)
        return res
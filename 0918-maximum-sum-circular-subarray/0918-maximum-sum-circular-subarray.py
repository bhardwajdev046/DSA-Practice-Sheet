class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n=len(nums)
        total_sum=sum(nums)
        maxend=minend=nums[0]
        maxsum=minsum=nums[0]
        for i in range(1,n):
            maxend=max(maxend+nums[i],nums[i])
            maxsum=max(maxsum,maxend)

            minend=min(minend+nums[i],nums[i])
            minsum=min(minsum,minend)
            circular_sum=total_sum-minsum
        if maxsum>0:
            return max(maxsum, circular_sum)
        else:
            return maxsum
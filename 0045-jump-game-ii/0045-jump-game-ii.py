class Solution:
    def jump(self, nums: List[int]) -> int:
        cache={}
        def helper(i,nums):
            if i>=len(nums)-1:
                return 0
            if i in cache:
                return cache[i]
            if nums[i]==0:
                return float('inf')
            min_steps=float('inf')
            for s in range(1,nums[i]+1):
                ans=1+helper(i+s,nums)
                min_steps=min(min_steps,ans)

            cache[i]=min_steps
            return min_steps
        return helper(0,nums)
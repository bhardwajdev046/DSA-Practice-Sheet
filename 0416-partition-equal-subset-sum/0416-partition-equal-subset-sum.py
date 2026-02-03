class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        temp=sum(nums)
        if temp%2==0:
            target=temp//2
        else:
            return False     
        i=len(nums)
        def fun(i,nums,target,dp):
            if i==0:
                return nums[0]==target
            if target==0:
                return True
            if dp[i][target]!=-1:
                return dp[i][target] 
            pick=False
            if nums[i]<=target:
                pick=fun(i-1,nums,target-nums[i],dp)
            notpick=fun(i-1,nums,target,dp)
            dp[i][target]=pick or notpick
            return dp[i][target]
        dp=[[-1]*(target+1) for _ in range(i)]
        return fun(i-1,nums,target,dp)
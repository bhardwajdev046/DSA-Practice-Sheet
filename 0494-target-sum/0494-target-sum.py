class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total=sum(nums)
        diff=(total-target)//2
        if (total-target)<0:
            return 0
        if (total-target)%2!=0:
            return 0
        def fun(i,diff,dp):
            if i==0:
                if diff==0 and nums[0]==0:
                    return 2
                if diff==0 or nums[0]==diff:
                    return 1
                return 0
            if dp[i][diff]!=-1:
                return dp[i][diff]
            pick=0
            if diff>=nums[i]:
                pick=fun(i-1,diff-nums[i],dp)
            notpick=fun(i-1,diff,dp)
            dp[i][diff]=pick+notpick
            return dp[i][diff]
        n=len(nums)
        dp=[[-1]*(diff+1) for _ in range(n)]
        return fun(n-1,diff,dp)
        
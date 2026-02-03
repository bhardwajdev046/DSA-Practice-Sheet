class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        temp=sum(nums)
        if temp%2!=0:
            return False 
        target=temp//2             
        i=len(nums)
        # def fun(i,target,dp):
        #     if i==0:
        #         return nums[i]==target
        #     if target==0:
        #         return True
        #     if dp[i][target]!=-1:
        #         return dp[i][target] 
        #     pick=False
        #     if nums[i]<=target:
        #         pick=fun(i-1,target-nums[i],dp)
        #     notpick=fun(i-1,target,dp)
        #     dp[i][target]=pick or notpick
        #     return dp[i][target]
        # dp=[[-1]*(target+1) for _ in range(i)]
        # return fun(i-1,target,dp) 

        # def fun(arr,sum):
        #     dp=[[False]*(sum +1) for _ in range(len(arr))]
            
        #     for i in range(len(arr)):
        #         dp[i][0]=True
        #     if arr[0]<=sum:
        #         dp[0][arr[0]]=True

        #     for i in range(1,len(arr)):
        #         for s in range(1,sum+1):
        #             if s>=arr[i]:
        #                 pick=dp[i-1][s-arr[i]]
        #             else:
        #                 pick=False
        #             notpick=dp[i-1][s]
            
        #             dp[i][s]=pick or notpick
        #     return dp[len(arr)-1][sum]
            
        # return fun(nums,target)

        def fun(arr,sum):
            prev=[False]*(sum +1)
            prev[0]=True
            if arr[0]<=sum:
                prev[arr[0]]=True

            for i in range(1,len(arr)):
                curr=[False]*(sum +1)
                curr[0]=True
                for s in range(1,sum+1):
                    if s>=arr[i]:
                        pick=prev[s-arr[i]]
                    else:
                        pick=False
                    notpick=prev[s]
                    curr[s]=pick or notpick
                prev=curr
            return prev[sum]
            
        return fun(nums,target)
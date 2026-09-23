class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        left=0
        mask=0
        res=-1
        for right in range(len(nums)):
            
            while mask & nums[right]!=0:
                mask^=nums[left]
                left+=1
            mask |= nums[right]
            
            res = max(res,right-left+1)
        return -1 if res==-1 else res
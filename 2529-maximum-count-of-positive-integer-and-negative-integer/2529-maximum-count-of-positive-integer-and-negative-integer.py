class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg=0
        pos=0
        zero=0
        i=0
        n=len(nums)
        while i<n and (nums[i]<=0):
            if nums[i]==0:
                zero+=1
            else:
                neg+=1
            i+=1
        pos=n-neg-zero
        return max(pos,neg)
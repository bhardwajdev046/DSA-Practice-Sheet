class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minindex=maxindex=res=nums[0]
        for i in range(1,len(nums)):
            c1=nums[i]
            c2=minindex*nums[i]
            c3=maxindex*nums[i]
            minindex=min(c1,c2,c3)
            maxindex=max(c1,c2,c3)
            res=max(res,max(minindex,maxindex))
        return res
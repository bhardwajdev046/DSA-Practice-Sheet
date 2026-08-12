class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix=nums[0]
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]!=1:
                break
            prefix+=nums[i]

        while prefix in nums:
            prefix+=1
        return prefix
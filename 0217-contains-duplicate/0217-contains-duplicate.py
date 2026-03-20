class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # freq={}
        # if len(nums)==1:
        #     return False

        # for x in nums:
        #     if x not in freq:
        #         freq[x]=1
        #     else:
        #         freq[x]+=1
        #         return True
        # return False

        nums=sorted(nums)
        if len(nums)==1:
            return False
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return True
        return False
            
            
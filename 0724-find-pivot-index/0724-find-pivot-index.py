class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalsum = sum(nums)
        prefixsum=0
        for i in range(len(nums)):
            
            suffixsum = totalsum - prefixsum -nums[i]
            if prefixsum==suffixsum:
                return i
            prefixsum+=nums[i]
        return -1

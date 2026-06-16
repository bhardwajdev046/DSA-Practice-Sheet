import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        add=0
        size=float('inf')
        left=0
        for right in range(len(nums)):
            add+=nums[right]
            while add >= target:
                size = min(size, right-left+1)
                add-=nums[left]
                left+=1
              
        # return 0 if sum(nums)<target else size

        # or

        return size if size!=float('inf') else 0
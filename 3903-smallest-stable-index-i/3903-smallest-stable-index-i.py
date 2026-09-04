class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        for i in range(len(nums)):
            mx = max(nums[:i+1])
            mn = min(nums[i:])
            score = mx-mn
            if score <= k:
                return i
        return -1
                
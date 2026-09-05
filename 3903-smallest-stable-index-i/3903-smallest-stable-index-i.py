class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        # for i in range(len(nums)):
        #     mx = max(nums[:i+1])
        #     mn = min(nums[i:])
        #     score = mx-mn
        #     if score <= k:          #BRUTE FORCE
        #         return i
        # return -1
                
        n = len(nums)
        suf = [0]*n
        suf[n-1] = nums[n-1]

        for i in range(n-2, -1, -1):
            suf[i] = min(suf[i+1], nums[i])
        
        maxi = 0
        for i in range(n):
            maxi = max(maxi, nums[i])
            if maxi-suf[i] <= k:
                return i
        return -1
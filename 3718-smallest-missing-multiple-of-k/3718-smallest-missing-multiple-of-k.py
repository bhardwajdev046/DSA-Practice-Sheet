class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        ans=0
        for i in range(1,len(nums)+1):
            if i*k not in nums:
                return i*k
            # i=i*k
        print(i)
        return (i+1)*k
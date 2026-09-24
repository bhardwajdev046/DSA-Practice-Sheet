class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n=nums[i]
            temp=0
            while n:
                temp+=n%10
                n=n//10
            if temp==i:
                return i
        return -1

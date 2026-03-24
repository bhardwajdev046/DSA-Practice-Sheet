class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for x in range(len(nums)):
            if nums[x]>=0:
                i=x
                j=x-1
                break
        else:
            i = len(nums)
            j = len(nums) - 1
        res=[]
        while j>=0 and i<len(nums):
            if abs(nums[i])<abs(nums[j]):
                res.append(nums[i]*nums[i])
                i+=1
            elif abs(nums[i])>=abs(nums[j]):
                res.append(nums[j]*nums[j])
                j-=1
        while i<len(nums):
            res.append(nums[i]*nums[i])
            i+=1
        while j>=0:
            res.append((nums[j]*nums[j]))
            j-=1
        return res
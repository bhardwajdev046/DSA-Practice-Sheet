from collections import Counter
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zeros,ones=0,0
        res=0
        hash={}
        for i in range(len(nums)):
            if nums[i]==0:
                zeros+=1
            else:
                ones+=1
            diff=zeros-ones
            if diff==0:
                res=max(res,i+1)
            if diff in hash:
                res=max(res,i-hash[diff])
            else:
                hash[diff]=i
        return res
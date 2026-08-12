class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        hash={}
        n=len(nums)
        low=0
        res=-1
        for high in range(n):
            hash[nums[high]]=hash.get(nums[high],0)+1
            while hash[nums[high]]>k:
                hash[nums[low]]-=1
                if hash[nums[low]]==0:
                    del hash[nums[low]]
                low+=1
            res=max(res,high-low+1)
        return res
            

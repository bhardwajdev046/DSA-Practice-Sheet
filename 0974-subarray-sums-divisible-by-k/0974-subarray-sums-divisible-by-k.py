class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixsum=0
        ans=0
        hash={0:1}
        for i in range(len(nums)):
            prefixsum+=nums[i]
            rem = prefixsum%k
            if rem<0:
                rem =rem+k
            if rem in hash:
                ans+=hash[rem]
            hash[rem] = hash.get(rem,0)+1
        return ans
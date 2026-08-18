class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        # temp=nums[:k]
        # subarray=[temp.copy()]
        # for right in range(k,len(nums)):
        #     temp.pop(0)
        #     temp.append(nums[right])
        #     subarray.append(temp.copy())
        # print(subarray)
        # hash={}
        # for x in set(nums):
        #     for arr in subarray:
        #         if x in arr:
        #             hash[x]=hash.get(x,0)+1
        # ans = -1
        # for x, freq in hash.items():
        #     if freq == 1:
        #         ans = max(ans, x)

        # return ans

        hash={}
        count=0
        for i in range(len(nums)-k+1):
            window = nums[i:i+k]
            for x in set(window):
                hash[x] = hash.get(x,0)+1
        ans=-1
        for x, freq in hash.items():
            if freq == 1:
                ans= max(ans,x)
        return ans

        return hash

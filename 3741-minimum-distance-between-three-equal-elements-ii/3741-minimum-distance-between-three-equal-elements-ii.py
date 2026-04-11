class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        hash={}
        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[nums[i]]=[]
            hash[nums[i]].append(i)
        mini=float('inf')
        for x in hash:
            idx=hash[x]
            if len(idx)>=3:
                for i in range(len(idx)-2):
                    a=idx[i]
                    c=idx[i+2]
                    ans=2*(c-a)
                    mini=min(mini,ans)
        return mini if mini!=float('inf') else -1
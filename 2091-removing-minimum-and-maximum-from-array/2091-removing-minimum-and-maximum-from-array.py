class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        maxi=max(nums)
        mini=min(nums)
        n=len(nums)
        hash={}
        for i in range(len(nums)):
            if nums[i] == maxi or nums[i] == mini:
                hash[nums[i]]=i
        print(hash)
        c1,c2,c3 = 0,0,0
        c1 = max(hash[maxi],hash[mini])+1
        c2 = max((n-hash[maxi]), (n-hash[mini])) 
        t1, t2 = 0, 0
        t1 = min(hash[maxi], hash[mini])+1
        t2 = min((n-hash[maxi]), (n-hash[mini]))
        c3 = t1+t2
        print((t1,t2))
        print([c1,c2])
        return min(c1,c2,c3)

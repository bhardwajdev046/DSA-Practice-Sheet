class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq={}
        if len(nums)==1:
            return False
        # for i in nums:
        #     freq[i]=freq.get(i,0)+1

        for x in nums:
            if x not in freq:
                freq[x]=1
            else:
                freq[x]+=1
                return True
        return False

        # for x in freq:
        #     if freq[x]>1:
        #         return True
        #     elif freq[x]<2 and x==len(freq)-1:
        #         return False
            
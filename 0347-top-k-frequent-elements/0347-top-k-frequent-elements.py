class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash={}
        res=[]
        
        for i in nums:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        temp=sorted(hash.items(),key=lambda x:x[1],reverse=True)
        for i in range(k):
            res.append(temp[i][0])
        return res

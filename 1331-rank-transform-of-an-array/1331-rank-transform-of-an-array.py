class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # hash={}
        # for i in range(len(arr)):
        #     hash[arr[i]]=hash.get(arr[i],0)+i+1
        #     ans=[]
        # for i in sorted(arr):
        #     ans.append(hash[i])
        # return hash
        arr1=sorted(arr)
        hash={}
        res=[]
        rank=1
        for i in arr1:
            if i not in hash:
                hash[i]=rank
                rank+=1

        for c in arr:
            res.append(hash[c])
        return res
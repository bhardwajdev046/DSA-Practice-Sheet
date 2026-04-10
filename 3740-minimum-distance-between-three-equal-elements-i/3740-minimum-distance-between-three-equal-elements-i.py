class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # hash={}
        # for i in nums:
        #     hash[i]=hash.get(i,0)+1
        # temp=[]
        # for i in hash:
        #     if hash[i]==3:
        #         temp.append(i)
        # mini=float('inf')
        # k=[]
        # for pair in temp:
        #     idx=[]
        #     for i in range(len(nums)):
        #         if nums[i]==pair:
        #             idx.append(i)
        #     ans=abs(idx[1]-idx[0])+abs(idx[2]-idx[1])+abs(idx[2]-idx[0])
        #     k.append(ans)
        #     idx.clear()
        # if k:
        #     return min(k)
        # else:
        #     return -1

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
                    b=idx[i+1]
                    c=idx[i+2]
                    ans=abs(a-b)+abs(b-c)+abs(c-a)
                    mini=min(mini,ans)
        return mini if mini!=float('inf') else -1
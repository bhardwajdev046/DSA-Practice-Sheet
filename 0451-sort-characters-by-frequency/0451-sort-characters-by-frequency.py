class Solution:
    def frequencySort(self, s: str) -> str:
        hash={}
        for ch in s:
            if ch in hash:
                hash[ch]+=1
            else:
                hash[ch]=1
        temp=sorted(hash.items(),key=lambda x:x[1],reverse=True)
        ans=[]
        for ch, count in temp:
            ans.append(ch * count)

        return "".join(ans)
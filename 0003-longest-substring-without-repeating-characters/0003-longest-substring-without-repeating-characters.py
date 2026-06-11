class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash={}
        low=0
        res=0
        for high in range(len(s)):
            hash[s[high]]=hash.get(s[high],0)+1
            
            while len(hash)<(high-low+1):
                hash[s[low]]-=1
                if hash[s[low]]==0:
                    del hash[s[low]]
                
                low+=1
            res=max(res,high-low+1)
        return res


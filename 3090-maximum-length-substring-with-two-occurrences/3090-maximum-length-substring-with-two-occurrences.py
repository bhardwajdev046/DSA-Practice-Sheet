class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        hash={}
        left=0
        res=0
        sett={i for i in s}
        for right in range(len(s)):
            hash[s[right]]=hash.get(s[right],0)+1
            while hash[s[right]]>2:
                hash[s[left]]-=1
                if hash[s[left]]==0:
                    del hash[s[left]]
                left+=1
            res=max(res,right-left+1)
        return res
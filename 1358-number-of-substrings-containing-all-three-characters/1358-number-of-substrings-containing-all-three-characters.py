class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left,right=0,0
        res=0
        hash={}
        for right in range(len(s)):
            hash[s[right]]=hash.get(s[right],0)+1
            while hash.get('a',0)!=0 and hash.get('b',0)!=0 and hash.get('c',0)!=0:
                res+=1
                res+=(len(s)-right-1)
                hash[s[left]]=hash.get(s[left],0)-1
                left+=1
        return res
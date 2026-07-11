class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash={}
        for i in range(len(s)):
            hash[s[i]] = hash.get(s[i],0)+1
        
        for i in range(len(s)):
            if hash[s[i]]==1:
                return i
        return -1

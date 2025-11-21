class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash={}
        for ch in s:
            hash[ch]=hash.get(ch,0)+1

        for i in range(len(s)):
            if hash[s[i]]!=1:
                continue
            else:
                return i

        return -1
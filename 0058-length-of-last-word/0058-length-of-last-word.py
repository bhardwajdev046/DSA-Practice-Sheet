class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        ch=len(s)-1
        while ch>=0 and s[ch]==' ':
            ch-=1
        while ch>=0 and s[ch]!=' ':
            count+=1
            ch-=1
        return count

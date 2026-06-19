class Solution:
    def fun(self,have,need):
        for ch in need:
            if have.get(ch,0) < need[ch]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        have={}
        need={}
        if len(s)<len(t):
            return ""
        for i in t:
            need[i]=need.get(i,0)+1
        low=0
        res=float('inf')

        for high in range(len(s)):
            have[s[high]] = have.get(s[high], 0) + 1
            while self.fun(have,need):
                leng=high-low+1
                if res>leng:
                    res=leng
                    start=low
                    
                have[s[low]]=have.get(s[low],0)-1
                if have[s[low]] == 0:
                    del have[s[low]]
                low+=1

        if res==float('inf'):
            return ''
        return s[start:start+res]

        
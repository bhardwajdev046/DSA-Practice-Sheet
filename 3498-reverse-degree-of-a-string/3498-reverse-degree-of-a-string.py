class Solution:
    def reverseDegree(self, s: str) -> int:
        store = {}
        i=26
        for x in "abcdefghijklmnopqrstuvwxyz":
            store[x]=store.get(x,i)
            i-=1
        res=0
        for i,ch in enumerate(s,start=1):
            if ch in store:
                temp=store[ch]
                res+=(temp*i)
        return res
            

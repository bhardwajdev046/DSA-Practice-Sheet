class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen=set()
        store=set()
        temp=''
        for i in range(len(s)-9):
            temp=s[i:i+10]
            if temp not in seen:
                seen.add(temp)
            else:
                store.add(temp)
        return list(store)
        
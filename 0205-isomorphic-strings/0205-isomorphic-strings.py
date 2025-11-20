class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_stot={}
        hash_ttos={}
        for i in range(len(s)):
            chars=s[i]
            chart=t[i]
            if chars in hash_stot:
                if hash_stot[chars]!=chart:
                    return False
            else:
                hash_stot[chars]=chart
            if chart in hash_ttos:
                if hash_ttos[chart]!=chars:
                    return False
            else:
                hash_ttos[chart]=chars
        return True
         
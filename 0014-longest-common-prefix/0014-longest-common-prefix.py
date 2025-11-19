class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base=strs[0]
        res=""
        for i in range(len(base)):
            for words in strs[1:]:
                if i==len(words) or base[i]!=words[i]:
                    return res
            res+=base[i]
        return res
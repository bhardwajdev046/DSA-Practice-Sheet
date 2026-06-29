class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        res=[]
        count=0
        # for i in range(len(word)):
        #     temp=""
        #     for j in range(i,len(word)):
        #         temp+=word[j]
        #         res.append(temp)
        # for k in patterns:
        #     if k in res:
        #         count+=1
        # return count
        for k in patterns:
            if k in word:
                count+=1
        return count
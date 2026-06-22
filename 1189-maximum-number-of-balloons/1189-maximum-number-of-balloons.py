class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq={}
        for ch in text:
            # if ch in hash:
            #     hash[ch]+=1
            # else:
            #     hash[ch]=1
            freq[ch]=freq.get(ch,0)+1
        # mini=float('inf')
        # for i in "balloon":
        #     mini=min(mini,hash.get(i,0))
        # return mini
        return min(
            freq.get('b', 0),
            freq.get('a', 0),
            freq.get('l', 0) // 2,
            freq.get('o', 0) // 2,
            freq.get('n', 0)
        )
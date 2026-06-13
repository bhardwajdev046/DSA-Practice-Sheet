class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        max_freq=0
        maxi=float('-inf')
        hash={}
        for right in range(len(s)):
            hash[s[right]]=hash.get(s[right],0)+1
            max_freq = max(max_freq, hash[s[right]])

            while ((right-left+1) - max_freq > k):
                hash[s[left]]-=1
                if hash[s[left]]==0:
                    del hash[s[left]]
                left +=1
            maxi = max(maxi, right-left+1)
        return maxi
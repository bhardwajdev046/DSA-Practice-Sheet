class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash={}
        for i in s:
            hash[i] = hash.get(i,0)+1
        flag=False
        ans=0
        for k in hash:
            if hash[k]%2==0:
                ans+=hash[k]
            else:
                if not flag:
                    ans+=hash[k]
                    flag=True
                else:
                    ans+=hash[k]-1
        return ans
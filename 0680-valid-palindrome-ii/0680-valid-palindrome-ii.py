class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispalindrome(st):
            left=0
            right=len(st)-1
            while left<right:
                if st[left]!=st[right]:
                    return False
                left+=1
                right-=1
            return True

        count=1
        left=0
        right=len(s)-1
        while left<right:
            if s[left]!=s[right] and count>0:
                f=ispalindrome(s[:left]+s[left+1:])
                t=ispalindrome(s[:right]+s[right+1:])
                return f or t

            left+=1
            right-=1
            
        return True


        
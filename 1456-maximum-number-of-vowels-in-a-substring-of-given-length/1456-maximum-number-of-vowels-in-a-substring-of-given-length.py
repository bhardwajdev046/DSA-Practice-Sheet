class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # vowels = 'aeiou'
        # n=len(s)
        # count = 0
        # maxi = 0
        # window=''

        # for i in range(k):
        #     window += s[i]
        #     if s[i] in vowels:
        #         count+=1
        
        # for right in range(k,n):
        #     window+=s[right]
        #     if s[right] in vowels:
        #         count+=1

        #     window=window[right-k+1:]
        #     if s[right-k] in vowels:
        #         count-=1

        vowels = 'aeiou'
        n=len(s)
        count = 0
        maxi = 0

        for i in range(k):
            if s[i] in vowels:
                count+=1
        
        maxi = count
        for right in range(k,n):
            if s[right] in vowels:
                count+=1

            if s[right-k] in vowels:
                count-=1

            maxi = max(maxi, count)
        return maxi

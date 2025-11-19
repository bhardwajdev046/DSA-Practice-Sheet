# class Solution:
#     def reverseWords(self, s: str) -> str:
#         ans=s.split()
#         # ans.reverse()
#         return " ".join(ans[::-1])
class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        n = len(s)
        i = 0
        
        # Extract words manually
        while i < n:
            # skip spaces
            while i < n and s[i] == " ":
                i += 1
            
            word = ""
            # collect characters of word
            while i < n and s[i] != " ":
                word += s[i]
                i += 1
            
            if len(word) > 0:
                words.append(word)
        
        # reverse word list manually
        l, r = 0, len(words) - 1
        while l < r:
            words[l], words[r] = words[r], words[l]
            l += 1
            r -= 1
        
        # build final answer manually
        ans = ""
        for i in range(len(words)):
            ans += words[i]
            if i != len(words) - 1:
                ans += " "
        
        return ans

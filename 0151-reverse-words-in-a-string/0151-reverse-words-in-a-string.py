class Solution:
    def reverseWords(self, s: str) -> str:
        ans=s.split()
        # ans.reverse()
        return " ".join(ans[::-1])
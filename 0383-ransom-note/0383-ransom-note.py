# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         count = [0] * 26

#         for ch in magazine:
#             count[ord(ch) - ord('a')] += 1

#         for ch in ransomNote:
#             if count[ord(ch) - ord('a')] != 0:
#                 count[ord(ch) - ord('a')] -= 1
#             else:
#                 return False

#         return True

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}
        for ch in magazine:
            count[ch] = count.get(ch,0) + 1            
        for ch in ransomNote:
            if count.get(ch,0) == 0 : 
                return False            
            count[ch] -= 1

        return True
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict1={}
        for i in strs:
            word="".join(sorted(i))
            if word in dict1:
                dict1[word].append(i)
            else:
               dict1[word]=[i]
        return list(dict1.values())


#METHOD:2 (without use sorting)

# from collections import defaultdict

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         anagram_map = defaultdict(list)

#         for word in strs:
#             # Create a 26-length count of characters (a-z)
#             count = [0] * 26
#             for char in word:
#                 count[ord(char) - ord('a')] += 1
            
#             # Use the tuple of counts as a key (tuples are hashable)
#             anagram_map[tuple(count)].append(word)

#         return list(anagram_map.values())

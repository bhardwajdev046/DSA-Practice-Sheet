from collections import deque 
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset=set(wordList)
        if endWord not in wordset:
            return 0
        queue=deque()
        queue.append((beginWord,1))
        while queue:
            word,level=queue.popleft()
            if word==endWord:
                return level
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == word[i]:
                        continue
                    newword=word[:i]+c+word[i+1:]
                    if newword in wordset:
                        queue.append((newword,level+1))
                        wordset.remove(newword)
        return 0
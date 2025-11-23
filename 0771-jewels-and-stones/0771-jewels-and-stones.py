class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hashset=set()
        for i in jewels:
            hashset.add(i)
            count=0
        for x in stones:
            if x in hashset:
                count+=1
        return count
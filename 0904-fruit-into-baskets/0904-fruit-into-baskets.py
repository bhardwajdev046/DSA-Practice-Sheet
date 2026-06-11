class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hash={}
        low=0
        res=-1
        for high in range(len(fruits)):
            hash[fruits[high]]=hash.get(fruits[high],0)+1
            while len(hash)>2:
                hash[fruits[low]]-=1
                if hash[fruits[low]]==0:
                    del hash[fruits[low]]
                low+=1

            if len(hash)<=2:
                res=max(res,high-low+1)
        return res

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # ans=0
        # for i in nums:
        #     ans ^=i
        # return True if ans==0 else False

        #above method fails in some test cases

        # hash = {}
        # for i in nums:
        #     hash[i] = hash.get(i,0)+1
        # for ele in hash:
        #     if hash[ele]%2 != 0:
        #         return False
        # return True

        #HASHMAP METHOD

        seen = set()
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)
        return len(seen) == 0

        #set method
class Solution:
    # def fact(self,n):
    #     if n<=1:
    #         return n
    #     return n*self.fact(n-1)

    def totalNumbers(self, digits: List[int]) -> int:
        # hash={}
        # even_count=0
        # n=len(digits)
        # for i in digits:
        #     if i%2==0:
        #         even_count+=1
        #     hash[i] = hash.get(i,0)+1
        # duplicate=1
        # for f in hash:
        #     duplicate*= self.fact(hash[f])
        #     print(duplicate)

        # res=0
        # res+= even_count*(n-1)*(n-2)
        # res//= duplicate
        # zero_count=self.fact(hash.get(0,0))

        # zero_comb = zero_count*(n-1)*(n-2)
        # if zero_count>0:
        #     zero_comb//=zero_count

        # return res-zero_comb
        hash = {}

        for i in digits:
            hash[i] = hash.get(i, 0) + 1

        ans = 0

        for i in range(1, 10):          # first digit
            for j in range(10):         # second digit
                for k in range(0, 10, 2):   # last digit even

                    need = {}

                    need[i] = need.get(i, 0) + 1
                    need[j] = need.get(j, 0) + 1
                    need[k] = need.get(k, 0) + 1

                    possible = True

                    for x in need:
                        if need[x] > hash.get(x, 0):
                            possible = False
                            break

                    if possible:
                        ans += 1

        return ans
        
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        # ans=0
        # i, j = 0, 0
        # n = len(nums)
        # temp=[]                            #BRUTE FORCE
        # for i in range(n):
        #     for j in range(i+1,n+1):
        #         temp.append(nums[i:j])
            
        # for s_arr in temp:
        #     myset = set()
        #     for i in s_arr:
        #         myset.add(i)
        #     ans += (len(myset))**2
        # return ans

        ans=0
        i, j = 0, 0
        n = len(nums)

        for i in range(n):
            myset = set()
            for j in range(i,n):
                
                myset.add(nums[j])
                ans += (len(myset))**2

        return ans
        
        
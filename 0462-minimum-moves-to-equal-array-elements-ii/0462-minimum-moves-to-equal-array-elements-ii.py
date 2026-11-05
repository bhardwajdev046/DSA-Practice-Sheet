class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        # n=len(nums)
        # nums.sort()
        # mid = 0
        # res = 0

        # if n%2 != 0:
        #     mid = nums[n//2]
        # else:
        #     if n == 2:
        #         mid = (nums[0]+nums[1])//2 
        #     else:
        #         k = n//2
        #         mid = (nums[k]+nums[k+1])//2
        
        # for i in nums:
        #     res += abs(mid - i)

        # return res

        n=len(nums)
        nums.sort()
        median = nums[n//2]
        moves = 0
        
        for i in nums:
            moves += abs(median - i)

        return moves

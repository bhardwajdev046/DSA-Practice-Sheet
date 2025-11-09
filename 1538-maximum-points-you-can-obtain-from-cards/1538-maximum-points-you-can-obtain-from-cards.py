class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        l=0
        r=k
        curr_sum=0
        for i in range(k):
            curr_sum+=nums[i]
        max_sum=curr_sum
        for _ in range(k):
            r-=1
            if l==0:
                l=len(nums)-1
            else:
                l-=1
            curr_sum = curr_sum + nums[l]-nums[r]
            max_sum=max(max_sum,curr_sum)
       
        return max_sum
        
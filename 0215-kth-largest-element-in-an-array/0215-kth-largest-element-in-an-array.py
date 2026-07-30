import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ans=[]
        for i in range(k):
            heapq,heappush(ans,nums[i])
        for i in range(k,len(nums)):
            if ans[0]<nums[i]:
                heapq.heappop(ans)
                heapq.heappush(ans,nums[i])
        return ans[0]
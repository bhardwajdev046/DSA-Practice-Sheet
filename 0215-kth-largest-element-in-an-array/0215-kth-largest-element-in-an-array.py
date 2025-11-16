import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ans=[]
        for i in range(k):
            heapq.heappush(ans,nums[i])
        for i in range(k,len(nums)):
            if nums[i]>ans[0]:
                heapq.heappop(ans)
                heapq.heappush(ans,nums[i])
        return ans[0]    
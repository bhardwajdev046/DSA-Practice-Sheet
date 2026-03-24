class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        low=0
        high=len(nums)-1
        while low<=high:
            sum=nums[low]+nums[high]
            if sum==target:
                return [low+1,high+1]
            elif sum>target:
                high-=1
            else:
                low+=1
                
            
        
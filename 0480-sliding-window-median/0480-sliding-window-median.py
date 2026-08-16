class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        left=0
        ans=[]
        temp=nums[left:left+k]
        temp.sort()
        mid=k//2
        if k%2!=0:
            ans.append(temp[mid])
        else:
            ans.append((temp[mid-1]+temp[mid])/2)
        for right in range(k,len(nums)):
            temp.remove(nums[left])
            temp.append(nums[right])
            left+=1
            temp.sort()
            mid=k//2
            if k%2!=0:
                ans.append(temp[mid])
            else:
                ans.append((temp[mid-1]+temp[mid])/2)
        return ans
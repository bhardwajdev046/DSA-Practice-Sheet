class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[0]*n
        suffix=[0]*n
        prefix[0]=nums[0]
        for i in range(1,n):
            prefix[i]=prefix[i-1]*nums[i]

        suffix[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            suffix[i]=suffix[i+1]*nums[i]
        temp=[0]*n
        for i in range(n):
            if i==0:
                temp[i]=suffix[i+1]
            elif i==n-1:
                temp[i]=prefix[n-2]
            else:
                temp[i]=prefix[i-1]*suffix[i+1]
        return temp
class Solution:
    def largestOddNumber(self, nums: str) -> str:
        # res=''
        # ans=num.split()
        # for i in ans:
        #     if int(i)%2!=0:
        #         res+=i
                
        # return res
        i=len(nums)-1
        while i>=0:
            if int(nums[i])%2!=0:
                return nums[:i+1]
            i-=1               
        return ""

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        n1=min(nums)
        n2=max(nums)
        maxi=float('-inf')
        for i in range(1,n2+1):
            if n1%i==0 and n2%i==0:
                maxi=max(maxi,i)
        return maxi
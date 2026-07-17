class Solution:
    def bouqets(self, bloomDay, days, k):
        bouquets=0
        flowers=0
        for x in bloomDay:
            if x<=days:
                flowers+=1
            else:
                bouquets+=flowers//k
                flowers=0
        bouquets+=flowers//k
        return bouquets
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low=min(bloomDay)
        high=max(bloomDay)
        ans=-1
        if m*k > len(bloomDay):
            return -1
        while low<=high:
            days=(low+high)//2
            temp=self.bouqets(bloomDay, days, k)
            if temp<m:
                low=days+1
            else:
                ans=days
                high=days-1
        return ans
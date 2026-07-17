class Solution:
    def capacity(self, weights, wt, days):
        take=0
        t_day=0
        for x in weights:
            if take+x>wt:
                take=0
                t_day+=1
            take+=x
        if take:
            t_day+=1
        return t_day
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        ans=-1
        while low<=high:
            wt = (low+high)//2
            temp= self.capacity(weights, wt, days)
            if temp<=days:
                ans=wt
                high=wt-1
            else:
                low=wt+1
        return ans
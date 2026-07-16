class Solution:
    # def minEatingSpeed(self, piles: List[int], h: int) -> int:
    #     ans=-1
    #     low=1
    #     end=max(piles)
    #     while low<=end:
    #         speed=(low+end)//2
    #         time=0
    #         for i in range(len(piles)):
    #             time+=(piles[i])//speed
    #             if piles[i]%speed!=0:
    #                 time+=1
    #         if time>h:    #EAT with faster speed
    #             low=speed+1
    #         else:        #CHECK to try with slower speed 
    #             ans=speed
    #             end=speed-1
    #     return ans

    def hours(self, piles, n, speed):
        time=0
        for p in piles:
            time+=(p + speed -1)//speed
        return time
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans=-1
        low=1
        end=max(piles)
        n=len(piles)
        while low<=end:
            speed=(low+end)//2
            time=self.hours(piles,n,speed)
            if time>h:    #EAT with faster speed
                low=speed+1
            else:        #CHECK to try with slower speed 
                ans=speed
                end=speed-1
        return ans
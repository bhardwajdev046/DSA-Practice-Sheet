class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,101):
            temp=i
            dig=1
            while i:
                dig=dig*(i%10)
                i=i//10
            if dig%t==0:
                return temp
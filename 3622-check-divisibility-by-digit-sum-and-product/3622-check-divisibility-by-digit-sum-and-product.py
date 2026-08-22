class Solution:
    def checkDivisibility(self, n: int) -> bool:
        add = 0
        product = 1
        temp=n
        while temp:
            add+=temp%10
            product*=temp%10
            temp=temp//10
        temp = add+product
        return True if n%temp == 0 else False
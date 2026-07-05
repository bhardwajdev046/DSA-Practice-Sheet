class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for astrd in asteroids:
            while stack and astrd < 0 and stack[-1]>0:
                summ=astrd+stack[-1]
                if summ<0:
                    stack.pop()
                elif summ>0:
                    astrd=0
                else:
                    stack.pop()
                    astrd=0
            if astrd != 0:
                stack.append(astrd)
        return stack
                
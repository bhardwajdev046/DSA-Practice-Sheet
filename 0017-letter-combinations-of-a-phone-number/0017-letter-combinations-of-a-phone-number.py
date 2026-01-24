# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
    #     def fun(s1,s2,li):
    #         if len(s2)==0:
    #             li.append(s1)
    #             return li

    #         digit=int(s2[0])
    #         if digit==1 or digit==0:
    #             fun(s1,s2[1:],li)
    #             return
    #         if digit==7:
    #             start=(digit-2)*3
    #             end=start+4
    #         elif digit==9:
    #             start=((digit-2)*3)+1
    #             end=start+4
    #         elif digit==8:
    #             start=((digit-2)*3)+1
    #             end=start+3
    #         else:
    #             start=(digit-2)*3
    #             end=start+3
    #         for i in range(start,end):
    #             ch=chr(ord('a')+i)
    #             fun(s1+ch,s2[1:],li)
        
    #     li=[]
    #     a = fun("",digits,li)
    #     return li
        
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        keypad = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }
        
        result = []

        def backtrack(index, path):
            if index == len(digits):
                result.append(path)
                return
            for char in keypad[digits[index]]:
                backtrack(index + 1, path + char)

        backtrack(0, "")
        return result



        
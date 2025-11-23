class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # stacks=[]
        # stackt=[]
        # res1=""
        # res2=""
        # for ch in s:
        #     if ch!='#':
        #         stacks.append(ch)
        #     else:
        #         if stacks:
        #             stacks.pop()
        # res1+="".join(stacks)
        # for ch in t:
        #     if ch!='#':
        #         stackt.append(ch)          #MY Solution
        #     else:
        #         if stackt:
        #             stackt.pop()
        # res2+="".join(stackt)
        # if res1==res2:
        #     return True
        # else:
        #     return False

       
        def helper(string):
            count=0
            res=""
            for ch in string[::-1]:
                if ch=="#":
                    count+=1
                else:
                    if count>0:
                        count-=1
                    else:
                        res+=ch
            return res[::-1]
        
        return helper(s)==helper(t)

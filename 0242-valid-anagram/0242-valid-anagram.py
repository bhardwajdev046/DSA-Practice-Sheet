class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s)!=len(t):
        #     return False
        # s_sort=sorted(s)                            #SORT METHOD
        # t_sort=sorted(t)
        # if s_sort==t_sort:
        #     return True
        # return False
        
        hash={}
        if len(s)!=len(t):
            return False
        for i in s:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        for x in t:
            if x in hash:
                if hash[x]==0:
                    return False
                else:
                    hash[x]-=1
            elif x not in hash:
                return False
        return True
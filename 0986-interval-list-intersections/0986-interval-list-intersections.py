class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if len(firstList)==0 or len(secondList)==0:
            return []
        i,j=0,0
        s,e=0,0
        res=[]
        while i<len(firstList) and j<len(secondList):
            start1=firstList[i][0]
            end1=firstList[i][1]

            start2=secondList[j][0]
            end2=secondList[j][1]

            if start1<start2:
                if start2<=end1:
                    s=max(start1,start2)
                    e=min(end1,end2)
                    res.append([s,e])
            else:
                if start1<=end2:
                    s=max(start1,start2)
                    e=min(end1,end2)
                    res.append([s,e])
            if end1<end2:
                i+=1
            else:
                j+=1
        return res

            

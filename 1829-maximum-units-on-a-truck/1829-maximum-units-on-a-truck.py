class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:(x[1],x[0]),reverse=True)
        spaceleft=truckSize
        unit=0
        for i in range(len(boxTypes)):
            if spaceleft==0:
                break
            take=min(spaceleft,boxTypes[i][0])
            unit+=take*boxTypes[i][1]
            spaceleft-=take
        return unit
            # if count<=truckSize:
            #     count+=boxTypes[i][0]
            #     unit+=boxTypes[i][0]*boxTypes[i][1] 
            # while count>truckSize:
            #     count-=1
            #     unit-=(boxTypes[i][0]-1)*boxTypes[i][1]
                                                                                                                                                             
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        heap=[]
        n=len(stations)
        stations.sort()
        count=0
        i=0
        current_fuel=startFuel
        if len(stations)==0 and startFuel<target:
            return -1
        if len(stations)==0:
            return 0

        while current_fuel<target:
            while i<n and stations[i][0]<=current_fuel:
                heapq.heappush(heap,-stations[i][1])
                i+=1
            if len(heap)==0:
                return -1
            if current_fuel<target:
                current_fuel-=heapq.heappop(heap)
            count+=1
        return count
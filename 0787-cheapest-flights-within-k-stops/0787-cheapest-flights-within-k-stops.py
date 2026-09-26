class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        lst=[[] for _ in range(n)]
        for u,v,w in flights:
            lst[u].append([v,w])
        q=deque()
        price=[float('inf')]*n
        q.append((0,0,src))
        price[src]=0

        while q:
            stop,old_p,node = q.popleft()

            for x,p in lst[node]:
                new_p = old_p + p
                if new_p < price[x]:
                    if stop==k:
                        if x != dst:
                            continue
                    price[x]=new_p
                    q.append((stop+1,new_p,x))
        
        return -1 if price[dst]==float('inf') else price[dst]
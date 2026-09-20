class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0] * n
        component = 0
        q = deque()
        for i in range(n):
            if visited[i] == 0:
                component += 1
                q.append(i)
                visited[i] = 1

                while q:
                    node = q.popleft()
                    for j in range(n):
                        if isConnected[node][j] == 1 and visited[j] == 0:
                            q.append(j)
                            visited[j] = 1

        return component
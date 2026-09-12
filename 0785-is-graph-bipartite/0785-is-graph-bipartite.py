class Solution:
    def dfs(self, node, visited, graph, color):
        visited[node]=color
        for x in graph[node]:
            if visited[x]!=-1:
                if visited[x]==color:
                    return False
            else:
                ans = self.dfs(x,visited,graph,1-color)
                if ans==False:
                    return False
        return True


    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [-1]*n
        for node in range(n):
            if visited[node]!=-1:
                continue
            ans = self.dfs(node, visited, graph, 0)
            if ans==False:
                return False
        return True
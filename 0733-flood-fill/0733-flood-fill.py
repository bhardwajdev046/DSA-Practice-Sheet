class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        row=len(image)
        col=len(image[0])
        visited=[[0]*col for _ in range(row)]
        org = image[sr][sc]
        def dfs(i,j):
            if i<0 or i>=row or j<0 or j>=col:
                return image
            if image[i][j]==color:
                return image
            if image[i][j]!=org:
                return image
            if visited[i][j]!=0:
                return image
            visited[i][j]=1
            image[i][j]=color
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
            
            return image
        return dfs(sr,sc)
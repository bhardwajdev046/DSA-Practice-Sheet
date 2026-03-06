class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:
            return image
        initial_color=image[sr][sc]
        rows=len(image)
        cols=len(image[0])
        
        # def dfs(r,c):
        #     if r<0 or r>=rows or c<0 or c>=cols:
        #         return
        #     if image[r][c]!=initial_color:
        #         return
        #     if image[r][c]==color:
        #         return
        #     image[r][c]=color
        #     for dx,dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        #         dfs(r+dx,c+dy)
        #     return image
        # return dfs(sr,sc)

        queue=deque()
        queue.append((sr,sc))
        while queue:
            r,c=queue.popleft()
            image[r][c]=color
            for dx,dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                new_r=dx+r
                new_c=dy+c
                if new_r<0 or new_c<0 or new_r>=rows or new_c>=cols:
                    continue
                if image[new_r][new_c]!=initial_color:
                    continue
                if image[new_r][new_c]==color:
                    continue
                queue.append((new_r,new_c))
        return image
                
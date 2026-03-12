class Solution:
    def dfs(self,r,c,board,visited):
        if r<0 or c<0 or r>=len(board) or c>=len(board[0]):
            return
        if visited[r][c]==1:
            return
        if board[r][c] != 'O':
            return
        visited[r][c]=1
        for dx,dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            self.dfs(r+dx,c+dy,board,visited)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """ 
        row=len(board)
        col=len(board[0])
        visited=[[0]*(col) for _ in range(row)]
        for c in range(col):
            if board[0][c] == 'O':
                self.dfs(0, c, board, visited)
            if board[row-1][c] == 'O':
                self.dfs(row-1, c, board, visited)

        for r in range(row):
            if board[r][0] == 'O':
                self.dfs(r, 0, board, visited)
            if board[r][col-1] == 'O':
                self.dfs(r, col-1, board, visited)
        for r in range(row):
            for c in range(col):
                if visited[r][c]!=1 and board[r][c]=='O':
                    board[r][c]="X"
        
        
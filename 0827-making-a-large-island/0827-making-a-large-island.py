class Solution:
    def dfs(self,i, j, island_id, grid):
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]):
            return 0
        if grid[i][j] != 1:
            return 0

        grid[i][j] = island_id
        size = 1
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr = i + dx
            nc = j + dy
            size += self.dfs(nr, nc, island_id, grid)
        return size

    def largestIsland(self, grid: list[list[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        visited = [[0] * row for _ in range(row)]
        island_size = {}
        island_id = 2

    # Step 1: Find all existing islands and their sizes
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    size = self.dfs(i, j, island_id, grid)
                    island_size[island_id] = size
                    island_id += 1

    # Step 2: Find the maximum island size after one flip
        max_size = max(island_size.values(), default=0)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    unique_islands = set()
                    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        nr = i + dx
                        nc = j + dy
                        if 0 <= nr < row and 0 <= nc < col:
                            if grid[nr][nc] > 1:
                                unique_islands.add(grid[nr][nc])
                    size = 1
                    for island in unique_islands:
                        size += island_size[island]
                    max_size = max(max_size, size)

        # Step 3: Handle all-water grid
        if max_size == 0:
            max_size = 1

        return max_size
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        island = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    island +=1
                    self.visit(i, j, grid)
        return island

    def visit(self, row, col, grid):
        n = len(grid)
        m = len(grid[0])

        dx = [1, -1, 0 ,0]
        dy = [0 ,0, 1, -1]

        if 0 <= row < n and 0 <= col < m and grid[row][col] == '1':
            grid[row][col] = '2'
            for i in range(4):
                self.visit(row + dx[i], col + dy[i], grid)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        fresh = 0
        time = 0
        queue = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                if grid[i][j] == 1:
                    fresh +=1
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            row, col, t = queue.popleft()
            time = max(time, t)
            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy

                if 0 <= new_row < n and 0 <= new_col < m and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    fresh -=1
                    queue.append((new_row, new_col, t + 1))
        return time if fresh == 0 else -1
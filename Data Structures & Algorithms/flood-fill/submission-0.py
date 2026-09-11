class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        init_color = image[sr][sc]
        if init_color == color:
            return image
        
        self.dfs(sr, sc, image, color, init_color)
        return image

    def dfs(self, row, col, image, color, init_color):
        n = len(image)
        m = len(image[0])
        
        if 0 <= row < n and 0 <= col < m and image[row][col] == init_color:
            image[row][col] = color
            self.dfs(row + 1, col, image, color, init_color) # down
            self.dfs(row - 1, col, image, color, init_color) # dup
            self.dfs(row, col + 1, image, color, init_color) # right
            self.dfs(row, col - 1, image, color, init_color) # left

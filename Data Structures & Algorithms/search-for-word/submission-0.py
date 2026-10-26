class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])

        def dfs(row, col, start):
            if len(word) == start:
                return True
            
            if 0 > row or row >= n or 0 > col or col >=m or board[row][col] != word[start]:
                return False
        
            temp = board[row][col]
            board[row][col] = '0'

            found = dfs(row + 1, col, start + 1) or dfs(row - 1, col, start + 1) or dfs(row, col + 1, start + 1) or dfs(row, col - 1, start + 1)

            board[row][col] = temp
            return found
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False

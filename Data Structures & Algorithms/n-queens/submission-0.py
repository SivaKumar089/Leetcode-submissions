class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def isValid(board, row, col):
            # back row
            for i in range(col):
                if board[row][i] == 'Q':
                    return False
            
            i = row - 1
            j = col - 1

            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -=1
                j -=1

            i = row + 1
            j = col- 1

            while i < n and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i +=1
                j -=1
            return True 

        
        def backtrack(col):
            if n == col:
                res.append(["".join(r) for r in board])
                return 
            
            for row in range(n):
                if isValid(board, row, col):
                    board[row][col] = 'Q'
                    backtrack(col + 1)
                    board[row][col] = "."


        
        res = []
        board = [["."] * n for _ in range(n)]
        backtrack(0)
        return res
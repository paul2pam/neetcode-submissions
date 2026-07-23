class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        def dfs(i, j):
            
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[i]) or board[i][j] == "X":
                return
            if board[i][j] == "O":
                board[i][j] = "Y"
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)
        
        for i in range(len(board)):
            dfs(i, 0)
            dfs(i, len(board[i]) - 1)
        for j in range(len(board[i])):
            dfs(0, j)
            dfs(len(board) - 1, j)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "Y":
                    board[i][j] = "O"
        
                
            
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i : set() for i in range(9)}
        cols = {i : set() for i in range(9)}
        blocks = {i : set() for i in range(9)}
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                block = (r // 3) * 3 + (c // 3)
                if (board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in blocks[block]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                blocks[block].add(board[r][c])

        return True
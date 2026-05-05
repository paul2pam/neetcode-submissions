from collections import deque

class Solution:
    def inbounds(self, board, i, j):
        if (i >= len(board) or i < 0):
            return False
        elif (j >= len(board[i]) or j < 0):
            return False
        else:
            return True

    def dfs(self, board, word, i, j, formed):
        
        if not self.inbounds(board, i, j):
            return
        if board[i][j] != word[len(formed)]:
            return
        if (i, j) in self.d:
            return
        if len(formed) == len(word) - 1:
            
            print("appending " + formed + board[i][j])
            self.lst.append(formed + board[i][j])
            return

        self.d[(i, j)] = True

        formed += board[i][j]
        #print(formed)
        self.dfs(board, word, i+1, j, formed)
        self.dfs(board, word, i-1, j, formed)
    
        self.dfs(board, word, i, j+1, formed)
        self.dfs(board, word, i, j-1, formed)

        del self.d[(i, j)]
        



    def exist(self, board: List[List[str]], word: str) -> bool:
        self.d = {}
        self.lst = []
        ret = False
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (board[i][j] == word[0]):
                    self.d.clear()
                    self.dfs(board, word, i, j, "")
        
        for item in self.lst:
            #print(item)
            if item == word:
                return True
        return False
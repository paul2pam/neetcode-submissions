class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                new = Node()
                curr.children[char] = new
                curr = new
            else:
                curr = curr.children[char]
        
        curr.end = True

    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            else:
                curr = curr.children[char]

        return curr.end

    def starts_with(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            else:
                curr = curr.children[char]
        return True
            

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        maxLen = 0
        t = Trie()
        for word in words:
            t.insert(word)

        res = []

        def dfs(i, j, word):
            
            
            if i < 0 or i == len(board):
                return 
            if j < 0 or j == len(board[0]):
                return 
            if ((i, j) in visited):
                return

            if not t.starts_with(word):
                return

            word += board[i][j]
            visited.add((i, j))

            if t.search(word) and word not in res:
                res.append(word)

            dfs(i + 1, j, word)  
            dfs(i - 1, j, word)  
            dfs(i, j + 1, word)  
            dfs(i, j - 1, word)
            visited.remove((i, j))

        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                dfs(i, j, "")

        return res


        

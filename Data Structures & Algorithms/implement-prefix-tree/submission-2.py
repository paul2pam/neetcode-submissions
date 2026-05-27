class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                new = Node()
                curr.children[char] = new
                curr = new
            else:
                curr = curr.children[char]
            
        curr.end = True


    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            else:
                curr = curr.children[char]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            else:
                curr = curr.children[char]
        return True
        
        
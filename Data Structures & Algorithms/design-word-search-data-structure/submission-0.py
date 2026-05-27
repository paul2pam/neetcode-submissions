class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
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

        for i, char in enumerate(word):
            if char == '.':
                for child in curr.children:
                    tryword = word[: i] + child + word[i + 1:]
                    if self.search(tryword):
                        return True
            if char not in curr.children:
                return False
            else:
                curr = curr.children[char]
        
        return curr.end

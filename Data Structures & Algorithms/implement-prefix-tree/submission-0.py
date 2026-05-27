class PrefixTree:

    def __init__(self):
        self.data = []


    def insert(self, word: str) -> None:
        self.data.append(word)


    def search(self, word: str) -> bool:
        for existing_word in self.data:
            if word == existing_word:
                return True
        return False


    def startsWith(self, prefix: str) -> bool:
        length = len(prefix)
        for existing_word in self.data:
            if len(existing_word) >= len(prefix) and existing_word[:length] == prefix:
                return True
        return False
        
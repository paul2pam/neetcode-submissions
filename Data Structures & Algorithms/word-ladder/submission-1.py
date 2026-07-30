class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if beginWord not in wordList:
            wordList.append(beginWord)
        graph = {word : [] for word in wordList}

        def off_by_one(word1, word2):
            count_diff = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    count_diff += 1
            if count_diff == 1:
                return True
            else:
                return False

        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if off_by_one(wordList[i], wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])
        

        q = deque()
        d = {word: float("INF") for word in wordList}
        q.append(beginWord)
        d[beginWord] = 1
        visited = set()

        while q:
            curr = q.popleft()
            if curr == endWord:
                print(d)
                return d[endWord]
            visited.add(curr)
            for neighbour in graph[curr]:
                if neighbour not in visited:
                    d[neighbour] = min(d[neighbour], 1 + d[curr])
                    q.append(neighbour)
        
        return 0




        


        
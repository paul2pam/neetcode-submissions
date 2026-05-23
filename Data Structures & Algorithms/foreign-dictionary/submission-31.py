class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        all_chars = []

        for word in words:
            for c in word:
                if c not in all_chars:
                    all_chars.append(c)
        print(all_chars)

        leq = {char: [] for char in all_chars}

        for i in range(0, len(words) - 1):
            word = words[i]
            next_word = words[i + 1]

            j = 0
            while j < len(next_word) and j < len(word):
                if (next_word[j] == word[j]):
                    j += 1
                else:
                    if next_word[j] not in leq[word[j]]:
                        leq[word[j]].append(next_word[j])
                    break
            if j < len(word) and j == len(next_word):
                return ""
                    

        print(leq.items())

        visited = set()

        def dfs(c, string):
            print(c, string)
            if c not in leq :
                return c + string
            for less in leq[c]:
                if less in visited:
                    continue
                visited.add(less)
                string = dfs(less, string)

            return c + string 

        def has_cycle(c):
            visit = set()
            cycle = set()

            def depth(char):
                visit.add(char)
                cycle.add(char)

                for neighbor in leq[char]:
                    if neighbor in cycle:
                        return True
                    if neighbor not in visit:
                        if depth(neighbor):
                            return True
                cycle.remove(char)
                return False

            for char in all_chars:
                if char not in visit:
                    if depth(char):
                        return True
            return False
            
        if has_cycle(words[0][0]):
            return ""
        #string = dfs(words[0][0], "")
        
        #leftover characters
        print("test")
        string = ""
        print(all_chars)
        for char in all_chars:
            visited.clear()
            print(f"trying out {char}")
            new_string = dfs(char, "")
            if len(new_string) > len(string):
                string = new_string
                print(f"char {char} made string {string}")
            skip = False


            for char in new_string:
                if char in string:
                    skip = True
            
            if not skip:
                string = new_string + string
            
            
        for char in all_chars:
            if char not in string:
                string += char
        
        return string
        


        
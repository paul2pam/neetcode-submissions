class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        m = {}

        for edge in edges:
            if edge[0] not in m:
                m[edge[0]] = []
            m[edge[0]].append(edge[1])

            if edge[1] not in m:
                m[edge[1]] = []
            m[edge[1]].append(edge[0])
        
        visited = set()
        def dfs(node, neighbors):
            print(node, neighbors)
            print(visited)
            visited.add(node)
            for neighbor in neighbors:
                if neighbor not in visited:
                    dfs(neighbor, m[neighbor])


        res = 0
        for node, neighbors in m.items():
            if node not in visited:

                dfs(node, neighbors)

                res += 1

        if len(m.items()) < n:
            res += (n - len(m.items()))
        return res
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adj = { i:[] for i in range(n)}

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
    
        visited = set()
        def dfs(i, prev):
            if i in visited:
                return False
            
            visited.add(i)
            for neighbor in adj[i]:
                if neighbor == prev:
                    continue
                if not (dfs(neighbor, i)):
                    return False
            return True

        return dfs(0, -1) and (len(visited) == n)

        


class DSU:
    def __init__(self, n):
        self.arr = [i for i in range(n)]
        self.rank = [1] * (n)
    
    def union(self, i, j):
        par_i = self.find(i)
        par_j = self.find(j)
        if par_i == par_j:
            return False
        if self.rank[par_i] > self.rank[par_j]:
            self.rank[par_i] += self.rank[par_j]
            self.arr[par_j] = par_i
        else:
            self.rank[par_j] += self.rank[par_i]
            self.arr[par_i] = par_j
        return True
    
    def find(self, i):
        
        while i != self.arr[i]:
            i = self.arr[i]
        return i



class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        dsu = DSU(len(edges) + 1)

        for edge in edges:
            if not dsu.union(edge[0], edge[1]):
                return edge

        return []

        
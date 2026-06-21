class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        res = []
        for point in points: 
            x = point[0]
            y = point[1]
            distance = (x**2 + y**2)**0.5
            
            heapq.heappush(h, (distance, x, y))
        
        for elem in heapq.nsmallest(k, h): 
            print(elem)
            elem = elem[1:]
            res.append(elem)
            
        return res

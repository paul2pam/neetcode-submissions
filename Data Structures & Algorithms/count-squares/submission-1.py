class CountSquares:

    def __init__(self):
        self.points = []
        self.pointset = {}

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.pointset[tuple(point)] = self.pointset.get(tuple(point), 0) + 1

    def count(self, point: List[int]) -> int:
        print("counting")
        res = 0
        for point2 in self.points: 
            
            if abs(point2[0] - point[0]) == abs(point2[1] - point[1]) and point2[0] - point[0] != 0:
                print(point, point2)
                if (point2[0], point[1]) in self.pointset and (point[0], point2[1]) in self.pointset:
                    res += self.pointset[(point2[0], point[1])] * self.pointset[(point[0], point2[1])]
        return res

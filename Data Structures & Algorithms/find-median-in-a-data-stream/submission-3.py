class MedianFinder:

    def __init__(self):
        self.l = []
        self.r = []
        self.median = None

    def addNum(self, num: int) -> None:
        #we first naively insert
        if (len(self.l) == len(self.r)):
            heapq.heappush(self.l, -num)
        else:
            heapq.heappush(self.r, num)

        #we then swap the boundaries
        if len(self.r) > 0 and (-(self.l[0]) > self.r[0]):
            #print(f"swapping boundaries: {self.l}, {self.r})")
            #if we find that our left portion has a higher max than 
            #our right portion's lowest min, we have to swap their lowest
            #and highest values 
            heapq.heappush(self.r, -heapq.heappop(self.l))
            heapq.heappush(self.l, -heapq.heappop(self.r))
            



    def findMedian(self) -> float:
        #print(f"finding median: {self.l}, {self.r}")
        if len(self.l) > len(self.r):
            return -(self.l[0])
        else:
            return (-(self.l[0]) + self.r[0]) / 2
        
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        h = []
        d = {}

        for task in tasks:
            d[task] = d.get(task, 0) + 1
                        
        for task, count in d.items():
            heapq.heappush(h, -count)
        
        cooldown = []
        time = 0

        while len(h) > 0 or len(cooldown) > 0:
            curr = 0
            if len(h) > 0:
                curr = heapq.heappop(h)
            if curr < -1:
                cooldown.append((curr + 1, time + n))
            time += 1
            if len(cooldown) > 0 and cooldown[0][1] < time:
                heapq.heappush(h, cooldown[0][0])
                cooldown = cooldown[1:]
            #print(h, cooldown, time)

        return time
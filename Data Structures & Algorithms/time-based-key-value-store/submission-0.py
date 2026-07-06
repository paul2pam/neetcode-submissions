class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key] = self.d.get(key, [])
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d or self.d[key] is None:
            return ""
        res = ""
        res_timestamp = -1
        print(self.d[key])
        for i, entry in enumerate(self.d[key]):
            if entry[0] <= timestamp and entry[0] > res_timestamp:
                res_timestamp = max(entry[0], res_timestamp)
                res = entry[1]
        return res


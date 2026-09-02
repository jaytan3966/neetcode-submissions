class TimeMap:

    def __init__(self):
        self.hashMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.hashMap.get(key, [])

        if not values: return ""

        l, r = 0, len(values)-1

        while l<=r:
            mid = (l+r)//2

            if values[mid][0] == timestamp: return values[mid][1]
            elif values[mid][0]>timestamp: r = mid-1
            else: l = mid+1

        return values[(l+r)//2][1] if r>=0 else ""

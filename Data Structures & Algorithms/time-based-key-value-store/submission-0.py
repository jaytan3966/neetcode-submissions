class TimeMap:

    def __init__(self):
        self.pairs = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.pairs[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.pairs[key]
        l, r = 0, len(arr)-1

        while l<=r:
            mid = (l+r)//2
            if arr[mid][1] == timestamp: return arr[mid][0]
            elif arr[mid][1] > timestamp: r = mid-1
            else: l = mid+1
        return arr[r][0]

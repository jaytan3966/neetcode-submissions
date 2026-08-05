class TimeMap:

    def __init__(self):
        self.pairs = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.pairs[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.pairs[key]
        n = len(arr)
        if n == 0: return ""

        l, r = 0, n-1

        if timestamp>arr[r][1]: return arr[r][0]
        if timestamp<arr[l][1]: return ""

        while l<=r:
            mid = (l+r)//2
            if arr[mid][1] == timestamp: return arr[mid][0]
            elif arr[mid][1] > timestamp: r = mid-1
            else: l = mid+1
        
        return arr[r][0]

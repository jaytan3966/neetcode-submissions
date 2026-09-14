class TimeMap:

    def __init__(self):
        self.hashMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashMap:
            self.hashMap[key] = []
        self.hashMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        ans = ""

        if key not in self.hashMap: return ans

        key_list = self.hashMap[key]
        l, r = 0, len(key_list)-1

        while l<=r:
            mid = (l+r)//2

            if key_list[mid][0] == timestamp: 
                return key_list[mid][1]
            elif key_list[mid][0] > timestamp: 
                r = mid-1
            else: 
                l = mid+1
                ans = key_list[mid][1]
        
        return ans


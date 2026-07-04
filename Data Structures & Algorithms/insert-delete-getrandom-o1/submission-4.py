class RandomizedSet:

    def __init__(self):
        self.seen = {}
        self.arr = []
        self.ind = 0
        self.n = 0

    def insert(self, val: int) -> bool:
        if val in self.seen: return False

        self.seen[val] = self.ind
        self.ind+=1
        self.n+=1
        self.arr.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.seen: return False

        ind = self.seen[val]
        del self.seen[val]

        lastElem = self.arr[self.n-1]
        self.arr[ind] = lastElem
        self.seen[lastElem] = ind

        self.arr.pop()
        self.ind-=1
        self.n-=1

        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
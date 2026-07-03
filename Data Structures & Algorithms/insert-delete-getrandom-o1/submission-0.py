class RandomizedSet:

    def __init__(self):
        self.valToInd = {}
        self.indToVal = {}
        self.ind = 0

    def insert(self, val: int) -> bool:
        if val in self.valToInd: return False

        self.valToInd[val] = self.ind
        self.indToVal[self.ind] = val
        self.ind+=1
        return True

    def remove(self, val: int) -> bool:
        if val in self.valToInd: 
            ind = self.valToInd[val]
            del self.valToInd[val]
            del self.indToVal[ind]
            return True
        return False

    def getRandom(self) -> int:
        ind = random.randint(0, self.ind-1)
        print(self.indToVal)
        return self.indToVal[ind]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
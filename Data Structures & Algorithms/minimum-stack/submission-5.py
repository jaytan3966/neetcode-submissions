class MinStack:

    def __init__(self):
        self.items = []
        self.mins = []

    def push(self, val: int) -> None:
        self.items.append(val)
        
        if not self.mins:
            self.mins.append(val)
        elif self.mins and self.mins[-1]>=val:
            self.mins.append(val)

    def pop(self) -> None:
        last = self.items.pop()

        if self.mins and self.mins[-1]==last:
            self.mins.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.mins[-1]

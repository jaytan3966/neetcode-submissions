class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.seen = {homepage:0}
        self.cur = 1

    def visit(self, url: str) -> None:
        self.history = self.history[:self.cur]
        if url in self.seen:
            ind = self.seen[url]
            self.cur = ind+1
        else:
            self.history.append(url)
            self.seen[url] = self.cur
            self.cur+=1

    def back(self, steps: int) -> str:
        if steps >= self.cur:
            self.cur = 1
            return self.history[0]
        self.cur-=steps
        print(self.history)
        return self.history[self.cur-1]

    def forward(self, steps: int) -> str:
        n = len(self.history)
        if self.cur+steps >= n:
            self.cur = n
            return self.history[n-1]
        self.cur+=steps
        print(self.history)
        return self.history[self.cur-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
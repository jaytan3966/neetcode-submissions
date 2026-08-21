class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.seen = {homepage:0}
        self.cur = 1
        self.leng = 1

    def visit(self, url: str) -> None:
        self.history = self.history[:self.cur]
        if url in self.seen:
            ind = self.seen[url]
            self.cur = ind+1
        else:
            self.history.append(url)
            self.seen[url] = self.cur
            self.cur+=1
            self.leng = self.cur

    def back(self, steps: int) -> str:
        if steps >= self.cur:
            self.cur = 1
            return self.history[0]
        self.cur-=steps

        return self.history[self.cur-1]

    def forward(self, steps: int) -> str:

        if self.cur+steps >= self.leng:
            self.cur = self.leng
            return self.history[self.leng-1]
        self.cur+=steps

        return self.history[self.cur-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
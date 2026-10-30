class Solution:
    def __init__(self):
        self.url = None
    def encode(self, longUrl: str) -> str:
        self.url = longUrl

        return longUrl
    def decode(self, shortUrl: str) -> str:
        return self.url

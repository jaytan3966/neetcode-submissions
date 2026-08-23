class Twitter:

    def __init__(self):
        self.tweetMap = defaultdict(list)
        self.connections = defaultdict(set)
        self.count = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((-self.count, tweetId))
        self.count+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.feed = []
        heapq.heapify(self.feed)
        connects = self.connections[userId]

        for tweet in self.tweetMap[userId]:
            heapq.heappush(self.feed, tweet)

        for connect in connects:
            for tweet in self.tweetMap[connect]:
                heapq.heappush(self.feed, tweet)
                if len(self.feed)>10:
                    heapq.heappop(self.feed)
        return [tweetId for count, tweetId in self.feed]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.connections[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.connections[followerId]:
            self.connections[followerId].remove(followeeId)

class Twitter:

    def __init__(self):
        self.tweetMap = defaultdict(list)
        self.connections = defaultdict(set)
        self.count = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((-self.count, tweetId))
        self.count+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.feed = [tweet for tweet in self.tweetMap[userId]]
        heapq.heapify(self.feed)
        connects = self.connections[userId] 

        for connect in connects:
            for tweet in self.tweetMap[connect]:
                if len(self.feed)>9:
                    heapq.heappop(self.feed)
                heapq.heappush(self.feed, tweet)

        ans = []
        while self.feed:
            cnt, latest = heapq.heappop(self.feed)
            ans.append(latest)
        return ans


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.connections[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.connections[followerId]:
            self.connections[followerId].remove(followeeId)

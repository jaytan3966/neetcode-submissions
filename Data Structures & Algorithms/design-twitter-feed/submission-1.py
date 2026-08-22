class Twitter:

    def __init__(self):
        self.tweets = []
        heapq.heapify(self.tweets)
        self.connections = defaultdict(set)
        self.cur = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = (-self.cur, (userId, tweetId))
        heapq.heappush(self.tweets, tweet)
        self.cur+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        cnt = 0
        ans = []
        cur = 0
        n = len(self.tweets)

        while cnt<10 and cur<n:
            i, tweet = self.tweets[cur]
            uid, tweetId = tweet[0], tweet[1]

            if uid == userId or uid in self.connections[userId]:
                ans.append(tweetId)
                cnt+=1
            cur+=1
        return ans


    def follow(self, followerId: int, followeeId: int) -> None:
        self.connections[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.connections[followerId]:
            self.connections[followerId].remove(followeeId)

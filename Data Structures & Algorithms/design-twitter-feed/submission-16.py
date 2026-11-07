from collections import defaultdict
class Twitter:

    def __init__(self):
        self.tweets = []
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((tweetId, userId))

        return
    def getNewsFeed(self, userId: int) -> List[int]:
        followers = self.followers[userId]

        news_feed = []
        cnt = 0
        for tweetId, user in self.tweets[::-1]:
            if user == userId or user in followers:
                news_feed.append(tweetId)
                cnt+=1
            if cnt == 10:
                break
        return news_feed
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

        return
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)

        return
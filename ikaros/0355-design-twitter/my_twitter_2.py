from typing import List

# 定义用户节点
class User:
    def __init__(self):
        self.follows = set()
        self.tweets = []

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = 0
        self.recent_max = 10
        self.tweets_time = {}
        self.users = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.users.setdefault(userId, User()).tweets.append(tweetId)
        self.time += 1
        self.tweets_time[tweetId] = self.time

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if userId not in self.users:
            return []
        ans = self.users[userId].tweets[-10:][::-1]
        for followed in self.users[userId].follows:
            if followed in self.users:
                followed_tweets = self.users[followed].tweets[-10:][::-1]
                i, j, combined = 0, 0, []
                while i < len(ans) and j < len(followed_tweets):
                    if self.tweets_time[ans[i]] > self.tweets_time[followed_tweets[j]]:
                        combined.append(ans[i])
                        i += 1
                    else:
                        combined.append(followed_tweets[j])
                        j += 1
                combined.extend(ans[i:])
                combined.extend(followed_tweets[j:])
                ans = combined[:10]
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId == followeeId:
            return True
        self.users.setdefault(followerId, User()).follows.add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId == followeeId:
            return True
        self.users.setdefault(followerId, User()).follows.discard(followeeId)   

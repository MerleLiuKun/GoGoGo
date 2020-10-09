from typing import List

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = 0
        self.posts_data = {}
        self.my_posts_data = {}
        self.follows_data = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.time += 1
        self.posts_data[tweetId] = self.time
        self.my_posts_data.setdefault(userId, []).append(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        follows = self.follows_data.get(userId)
        if follows is not None:
            follows.add(userId)
            follows = list(follows)
        else:
            follows = [userId]
        
        posts = []

        for uid in follows:
            posts.extend(self.my_posts_data.get(uid, []))
        
        return sorted(posts, key=lambda k: self.posts_data[k], reverse=True)[0:10]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follows_data.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follows_data.get(followerId, set()).discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1, 5)
print(obj.getNewsFeed(1))
obj.postTweet(2, 6)
obj.follow(1, 2)
print(obj.getNewsFeed(1))
print(obj.getNewsFeed(2))
obj.unfollow(1, 2)
print(obj.getNewsFeed(1))
print(obj.getNewsFeed(2))

"""
["Twitter","postTweet","unfollow","getNewsFeed"]
[[],[1,5],[1,1],[1]]
"""
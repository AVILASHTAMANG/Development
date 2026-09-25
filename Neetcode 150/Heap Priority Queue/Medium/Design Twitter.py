# Implement a simplified version of Twitter which allows users to post tweets, follow/unfollow each other, and view the
# 10 most recent tweets within their own news feed.
#
# Users and tweets are uniquely identified by their IDs (integers).
#
# Implement the following methods:
#
# Twitter() Initializes the twitter object.
# void postTweet(int userId, int tweetId) Publish a new tweet with ID tweetId by the user userId. You may assume that
# each tweetId is unique.
# List<Integer> getNewsFeed(int userId) Fetches at most the 10 most recent tweet IDs in the user's news feed.
# Each item must be posted by users who the user is following or by the user themself. Tweets IDs should be ordered
# from most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId follows the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId unfollows the user with ID followeeId.
import heapq
from typing import List

from collections import defaultdict
class Twitter:

    def __init__(self):
        self.time = 0
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []
        relevant_users = self.following[userId] | {userId}
        for user in relevant_users:
            for time, tweetId in self.tweets[user][-10:]:
                heapq.heappush(min_heap, (time, tweetId))
                if len(min_heap) > 10:
                    heapq.heappop(min_heap)

        res = []
        while min_heap:
            res.append(heapq.heappop(min_heap)[1])
        return res[::-1]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

if __name__ == "__main__":
    commands = [
        "Twitter",
        "postTweet",
        "postTweet",
        "getNewsFeed",
        "getNewsFeed",
        "follow",
        "getNewsFeed",
        "getNewsFeed",
        "unfollow",
        "getNewsFeed",
    ]
    args = [
        [],
        [1, 10],
        [2, 20],
        [1],
        [2],
        [1, 2],
        [1],
        [2],
        [1, 2],
        [1],
    ]

    output = []
    twitter = None

    for cmd, arg in zip(commands, args):
        if cmd == "Twitter":
            twitter = Twitter()
            output.append(None)
        elif cmd == "postTweet":
            twitter.postTweet(arg[0], arg[1])
            output.append(None)
        elif cmd == "getNewsFeed":
            output.append(twitter.getNewsFeed(arg[0]))
        elif cmd == "follow":
            twitter.follow(arg[0], arg[1])
            output.append(None)
        elif cmd == "unfollow":
            twitter.unfollow(arg[0], arg[1])
            output.append(None)

    print("Actual Output:  ", output)
    expected = [
        None,
        None,
        None,
        [10],
        [20],
        None,
        [20, 10],
        [20],
        None,
        [10],
    ]
    print("Expected Output:", expected)
    print("Match?          ", output == expected)

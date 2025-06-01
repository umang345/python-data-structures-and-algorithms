import heapq 
from typing import *

class Tweet:
    def __init__(self, userId, tweetId, counter):
        self.userId = userId
        self.tweetId = tweetId
        self.counter = counter

class Twitter:

    def __init__(self):
        self.users = dict()
        self.tweets = dict()
        self.counter = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        newTweet = Tweet(userId, tweetId,self.counter)
        self.counter+=1
        if self.users.get(userId) is None:
            self.users[userId] = set()
        if self.tweets.get(userId) is None:
            self.tweets[userId] = list()
        
        self.tweets[userId].append(newTweet)


    def getNewsFeed(self, userId: int) -> List[int]:
        '''
        For userId, I need to get all those this userId is following
        for every user, I need their tweets
        Then among all those tweets, I need to give latest 10
        '''
        if self.users.get(userId) is None:
            return []
        followers = self.users[userId]
        maxHeap = []
        if not self.tweets.get(userId) is None:
            maxHeap.append((-self.tweets[userId][-1].counter, len(self.tweets[userId])-1, self.tweets[userId]))


        for user in followers:
            tweets = self.tweets.get(user,[])
            if tweets:
                maxHeap.append((-tweets[-1].counter, len(tweets)-1,tweets))
        
        heapq.heapify(maxHeap)

        result = []
        while maxHeap and len(result)<10:
            counter, index, tweetList = heapq.heappop(maxHeap)
            result.append(tweetList[index].tweetId)

            if index > 0:
                heapq.heappush(maxHeap,(-tweetList[index-1].counter, index-1, tweetList))
        
        return result




    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if self.users.get(followerId) is None:
            self.users[followerId] = set()
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or self.users.get(followerId) is None or not followeeId in self.users[followerId]:
            return
        self.users[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
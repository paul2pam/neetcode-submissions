class Twitter:

    def __init__(self):
        self.following = {}
        self.stack = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.stack.append((userId, tweetId))
        if userId not in self.following:
            self.following[userId] = set()
        self.following[userId].add(userId)

    def getNewsFeed(self, userId: int) -> List[int]:
        print(self.stack)
        n = len(self.stack) - 1
        res = []
        for i in range(10):
            while n >= 0 and self.stack[n][0] not in self.following[userId] and self.stack[n][0] != userId:
                print(n)
                n -= 1
            if n < 0:
                break
            res.append(self.stack[n][1])
            n -= 1
            

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]:

            self.following[followerId].remove(followeeId)

class Solution:

    

    def coin(self, coins, amount):
        if amount in self.dp:
            return self.dp[amount]
        if (amount == 0):
            return 0
        tr = 9999
        for coin in coins:
            if (coin <= amount):
                tr = min(tr, self.coin(coins, amount - coin))
                
        self.dp[amount] = 1 + tr
        return 1 + tr

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.dp = {}
    
    
        coins = sorted(coins, reverse=True)

        x = self.coin(coins, amount)
        if (x >= 9999):
            return -1
        else:
            return x
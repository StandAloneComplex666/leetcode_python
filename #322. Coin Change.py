class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        INF = 0x7ffffffe
        dp = [0] + [INF] * amount 
        for i in xrange(amount + 1):
            for coin in coins:
                if i + coin <= amount:
                    dp[i+coin] = min(dp[i+coin],dp[i] + 1)
        return dp[amount] if dp[amount] != INF else -1
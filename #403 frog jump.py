#403 frog jump
class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        dp = {stone: {} for stone in stones}
        dp[0][0] = 0
        for stone in stones:
            for step in dp[stone].values():
                for k in [step + 1, step, step - 1]:
                    if k > 0 and stone + k in dp:
                        dp[stone + k][stone] = k
        return len(dp[stones[-1]].keys()) > 0
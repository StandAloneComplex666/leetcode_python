class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """       
        R, C = len(dungeon), len(dungeon[0])
        dp = [[0] * C for _ in range(R)]
        dp[-1][-1] = max(1 - dungeon[-1][-1], 1)
        for i in range(R - 2, -1, -1):
            dp[i][C - 1] = max(dp[i + 1][C - 1] - dungeon[i][C - 1], 1)
        for i in range(C - 2, -1, -1):
            dp[R - 1][i] = max(dp[R - 1][i + 1] - dungeon[R - 1][i], 1)
       
        for i in range(R - 2, -1, -1):
            for j in range(C - 2, -1, -1):
                # if adding health is much larger than health required, set it to 1
                dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 1)
        
        return dp[0][0] 
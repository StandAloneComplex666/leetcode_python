# 64. Minimum Path Sum
class Solution(object):  
    def minPathSum(self, grid):  
        """ 
        :type grid: List[List[int]] 
        :rtype: int 
        """  
        dp = [0]*len(grid)  
        dp[0] = grid[0][0]  
        for i in range(1,len(grid)) :  
            dp[i] = dp[i-1] + grid[i][0]  
        for j in range(1, len(grid[0])) :  
            for i in range(len(grid)) :  
                dp[i] = min(dp[i], dp[i-1]) + grid[i][j] if i > 0 else dp[i]+grid[i][j]  
        return dp[len(grid)-1]  
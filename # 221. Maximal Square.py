class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:return 0
        h,w = len(matrix),len(matrix[0])
        dp = [[0]*(w+1) for i in range(h+1)]
        solution = 0
        for i in range(1,h+1):
            for j in range(1,w+1):
                if matrix[i-1][j-1] == '0':continue
                dp[i][j] = 1+min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])
                solution = max(solution,dp[i][j]**2)
        return solution
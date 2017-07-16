#32ms /88.91%
import math
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        product = 1
        while n > 4:
            product *= 3
            n -= 3
        product *= n
        return product
#55ms/ 20.11%
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0, 1, 1, 2, 4, 6, 9]
        if n <= 6:
            return dp[n]
        return 3 * self.integerBreak(n - 3)
#172. Factorial Trailing Zeroes
#32ms / 92.03%
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 5
        res = 0
        while x <= n:
            res = res + n / x
            x = x * 5
        return res
# 650. 2 Keys Keyboard
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        def factors(n):
            d = 2
            while d * d <= n:
                while n % d == 0:
                    n /= d
                    yield d
                d += 1
            if n > 1:
                yield n

        return sum(factors(n))
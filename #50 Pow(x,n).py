#50 Pow(x,n) 46ms / 46.85%
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        import math
        current_x = x
        res = 1
        sign = 1
        if n == 0 :
            return 1
        if n < 0 :
            sign = -1
            n = abs(n)
        while n >= 1:
            if n % 2 == 1:
                res = res*current_x
            n = math.floor(n/2)
            current_x = current_x *current_x
        return res if sign == 1 else 1/res
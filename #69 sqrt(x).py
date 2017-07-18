#69.sqrt(x)//
class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x == 0:
            return 0
        i = 1; j = x / 2 + 1
        while( i <= j ):
            center = ( i + j ) / 2
            if center *center == x:
                return center
            elif center *center > x:
                j = center - 1
            else:
                i = center + 1
        return j

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        t = x
        while t * t > x:
            t = int(t / 2.0 + x / (2.0 * t))
        return t
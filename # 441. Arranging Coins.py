class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        num_rows = 0
        i = 1
        while(n>=i):
           num_rows += 1
           n = n - i
           i = i + 1
        return num_rows
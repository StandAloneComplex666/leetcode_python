#38 count and say/45ms/60.44%

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        for i in xrange(n-1):
            res = ''.join([str(len(list(group))) + digit for digit, group in itertools.groupby(res)])
        return res
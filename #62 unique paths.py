# unique path my version/49ms /20.02%
class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        if m == 1 and n == 1:
            list = [[1]]
        elif m == 1 and n > 1:
            list = [[1 for i in range(n)]]
        elif m > 1 and n == 1:
            list = [[1] for i in range(m)]
        else:
            list = [[0 for i in range(n)] for i in range(m)]
            for i in range(0, n):
                list[0][i] = 1
            for i in range(0, m):
                list[i][0] = 1
            for i in range(1, m):
                for j in range(1, n):
                    list[i][j] = list[i-1][j] + list[i][j-1]
        return list[m-1][n-1]

#unique path version 2 /28ms /99.47%
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ways = [1] * n
        for i in xrange(1, m):
            for j in xrange(1, n):
                ways[j] += ways[j - 1]
        return ways[n-1]
        
# 59. Spiral Matrix II
# my version
class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        if n == 0: return []
        matrix = [[0 for i in range(n)] for j in range(n)]
        up = 0; down = len(matrix)-1
        left = 0; right = len(matrix[0])-1
        direct = 0; count = 0
        while True:
            if direct == 0:
                for i in range(left, right+1):
                    count += 1; matrix[up][i] = count
                up += 1
            if direct == 1:
                for i in range(up, down+1):
                    count += 1; matrix[i][right] = count
                right -= 1
            if direct == 2:
                for i in range(right, left-1, -1):
                    count += 1; matrix[down][i] = count
                down -= 1
            if direct == 3:
                for i in range(down, up-1, -1):
                    count += 1; matrix[i][left] = count
                left += 1
            if count == n*n: return matrix
            direct = (direct+1) % 4

# fastest version
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for _ in xrange(n)]
        rt = 0
        rb = n-1
        cl = 0
        cr = n-1
        c = 1
        while rt < rb and cl < cr:
            for i in xrange(cl, cr):
                matrix[rt][i] = c
                c += 1
            for i in xrange(rt, rb):
                matrix[i][cr] = c
                c += 1
            for i in xrange(cr, cl, -1):
                matrix[rb][i] = c
                c += 1     
            for i in xrange(rb, rt, -1):
                matrix[i][cl] = c
                c += 1     
            cl += 1
            cr -= 1
            rt += 1
            rb -= 1
        if n%2 == 1:
            matrix[n/2][n/2] = c
        return matrix     
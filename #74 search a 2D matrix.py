#74 search a 2D matrix
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        if n == 0:
            return False
        
        x1, x2 = 0, m*n-1
        while x2 - x1 > 1:
            x3 = (x1+x2)/2
            a, b = x3/n, x3%n
            if matrix[a][b] > target:
                x2 = x3
            else:
                x1 = x3
        a, b = x1/n, x1%n
        if matrix[a][b] == target:
            return True
        a, b = x2/n, x2%n
        if matrix[a][b] == target:
            return True
        return False
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return
        self.accum = [[0 for i in range(len(matrix[0])+1)] for i in range(len(matrix)+1)]
        temp = 0
        for i in range(1,len(matrix)+1):
            temp = 0
            for j in range(1,len(matrix[0])+1):
                temp += matrix[i-1][j-1]
                self.accum[i][j] = temp + self.accum[i-1][j]
                
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        res  = self.accum[row2+1][col2+1] - self.accum[row2+1][col1] - self.accum[row1][col2+1] + self.accum[row1][col1]
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
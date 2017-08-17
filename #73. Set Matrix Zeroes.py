#  73. Set Matrix Zeroes
class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        m , n ,flag= len(matrix), len(matrix[0]),False       
        for i in range(m):
            if not matrix[i][0]: flag=True
            for j in range(1,n):
                if not matrix[i][j]:
                    matrix[i][0]=matrix[0][j]=0
        
        i = m - 1
        while i >= 0:
            j=n-1
            while j >=1:
                if (not matrix[i][0]) or (not matrix[0][j]):
                    matrix[i][j]=0
                j-=1
            if flag: matrix[i][0]=0
            i-=1
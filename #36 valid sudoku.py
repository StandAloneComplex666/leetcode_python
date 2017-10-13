#35 valid sudoku my version :I have not used set/92ms/36%
class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        def isValid(x, y, tmp):
            for i in range(9):
                if board[i][y]==tmp:return False
            for i in range(9):
                if board[x][i]==tmp:return False
            for i in range(3):
                for j in range(3):
                    if board[(x/3)*3+i][(y/3)*3+j]==tmp: return False
            return True
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':continue
                tmp=board[i][j]
                board[i][j]='D'
                if isValid(i,j,tmp)==False: return False
                else:
                    board[i][j]=tmp
        return True
# other's version: use set /58ms /99.73%
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        major_rows = [set() for i in range(9)]
        major_cols = [set() for i in range(9)]
        subsections = [[set() for j in range(3)] for i in range(3)]

        for row, row_list in enumerate(board):
            row_list = list(row_list)
            for col, val in enumerate(row_list):
                if val == '.':
                    continue
                if val in major_rows[row] or val in major_cols[col] or val in subsections[row//3][col//3]:
                    return False
                major_rows[row].add(val)
                major_cols[col].add(val)
                subsections[row//3][col//3].add(val)
        return True
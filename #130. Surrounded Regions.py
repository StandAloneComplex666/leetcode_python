#130. Surrounded Regions
class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solve(self, board):
        if not board or not board[0]:
            return
    
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            board[i] = list(board[i])
        
        for j in range(n):
            self.fill(board, 0, j)
            self.fill(board, m - 1, j)
            
        for i in range(m):
            self.fill(board, i, 0)
            self.fill(board, i, n - 1)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
        
    def fill(self, board, i, j):
        m = len(board)
        n = len(board[0])
        
        queue = [(i, j)]
        
        while queue:
            row, col = queue.pop(0)
            
            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != 'O':
                continue
            
            board[row][col] = '#'
            
            queue.append((row - 1, col))
            queue.append((row + 1, col))
            queue.append((row, col - 1))
            queue.append((row, col + 1))


sample 105 ms submission
import collections

class Solution(object):
    def dfs(self, board, i, j):
        m = len(board)
        n = len(board[0])
        #board[i][j] = ''

        if i-1 >= 0 and board[i-1][j] == 'O':
            board[i-1][j] = ''
            self.dfs(board, i, j)
        if i+1 < m and board[i+1][j] == 'O':
            board[i+1][j] = ''
            self.dfs(board, i+1, j)
        if j-1 >= 0 and board[i][j-1] == 'O':
            board[i][j-1] = ''
            self.dfs(board, i, j-1)
        if j+1 < n and board[i][j+1] == 'O':
            board[i][j+1] = ''
            self.dfs(board, i, j+1)

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return
        n = len(board[0])

        deque = collections.deque()
        for i in range(m):
            if board[i][0] == 'O':
                board[i][0] = ''
                deque.append([i, 0])
                #self.dfs(board, i, 0)
            if board[i][n-1] == 'O':
                board[i][n-1] = ''
                #self.dfs(board, i, n-1)
                deque.append([i, n-1])

        for j in range(n):
            if board[0][j] == 'O':
                board[0][j] = ''
                #self.dfs(board, 0, j)
                deque.append([0, j])
            if board[m-1][j] == 'O':
                board[m-1][j] = ''
                #self.dfs(board, m-1, j)
                deque.append([m-1, j])


        while deque:
            idx = deque.popleft()

            i, j = idx[0], idx[1]
            if i-1 >= 0 and board[i-1][j] == 'O':
                board[i-1][j] = ''
                deque.append([i-1, j])

            if i+1 < m and board[i+1][j] == 'O':
                board[i+1][j] = ''
                deque.append([i+1, j])

            if j-1 >= 0 and board[i][j-1] == 'O':
                board[i][j-1] = ''
                deque.append([i, j-1])

            if j+1 < n and board[i][j+1] == 'O':
                board[i][j+1] = ''
                deque.append([i, j+1])

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O': board[i][j] = 'X'
                if board[i][j] == '': board[i][j] = 'O'
                    
        #print(board)
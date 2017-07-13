#200 number of islands/202ms /18.05%
# DFS
class Solution:  
    # @param grid, a list of list of characters  
    # @return an integer  
    def numIslands(self, grid):  
        m = len(grid)  
        if m == 0:  
            return 0  
        n = len(grid[0])  
        visit = [[False for i in range(n)]for j in range(m)]  
        def check(x, y):  
            if x >= 0 and x<m and y>= 0 and y< n and grid[x][y] == '1' and visit[x][y] == False:  
                return True  
        def dfs(x,y):  
            nbrow = [1,0,-1,0]  
            nbcol = [0,1,0,-1]  
            for k in range(4):  
                newx = x + nbrow[k]  
                newy = y + nbcol[k]  
                if check(newx, newy):  
                    visit[newx][newy] = True  
                    dfs(newx,newy)  
        count = 0  
        for row in range(m):  
            for col in range(n):  
                if check(row,col):  
                    visit[row][col] = True  
                    dfs(row,col)  
                    count+=1  
        return count  
#BFS
class Solution:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        ans = 0
        if not len(grid):
            return ans
        m, n = len(grid), len(grid[0])
        visited = [ [False] * n for x in range(m) ] # m * n
        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1' and not visited[x][y]:
                    ans += 1
                    self.bfs(grid, visited, x, y, m, n)
        return ans

    def bfs(self, grid, visited, x, y, m, n):
        dz = zip( [1, 0, -1, 0], [0, 1, 0, -1] )
        queue = [ (x, y) ]
        visited[x][y] = True
        while queue:
            front = queue.pop(0)
            for p in dz:
                np = (front[0] + p[0], front[1] + p[1])
                if self.isValid(np, m, n) and grid[np[0]][np[1]] == '1' and not visited[np[0]][np[1]]:
                    visited[ np[0] ][ np[1] ] = True
                    queue.append(np)

    def isValid(self, np, m, n):
        return np[0] >= 0 and np[0] < m and np[1] >= 0 and np[1] < n
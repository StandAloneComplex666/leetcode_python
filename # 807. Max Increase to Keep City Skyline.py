class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxTopBottom = [0 for i in range(len(grid))]
        maxLeftRight = [0 for i in range(len(grid[0]))]
        
        for i in range(len(grid)):
            maxTopBottom[i] = max(grid[i])
        for j in range(len(grid[0])):
            temp = []
            for i in range(len(grid)):
                temp.append(grid[i][j])
            maxLeftRight[j] = max(temp)
            
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
               res += min(maxTopBottom[i], maxLeftRight[j]) - grid[i][j]
        return res


# others' version:
class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows_max = [max(row) for row in grid]
        columns = [[row[i] for row in grid] for i in range(len(grid))]
        cols_max = [max(col) for col in columns]
        increase = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                increase += min(rows_max[i], cols_max[j]) - grid[i][j]
        return increase
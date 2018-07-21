def swimInWater(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    maxH = 0
    q = []
    heapq.heappush(q, (grid[0][0], (0, 0)))
    while True:
        h, (x, y) = heapq.heappop(q)
        maxH = max(maxH, h)
        if (x, y) == (len(grid) - 1, len(grid[0]) - 1):
            return maxH
        grid[x][y] *= -1
        if x > 0 and grid[x - 1][y] >= 0:
            heapq.heappush(q, (grid[x - 1][y], (x - 1, y)))
        if x < len(grid) - 1 and grid[x + 1][y] >= 0:
            heapq.heappush(q, (grid[x + 1][y], (x + 1, y)))
        if y > 0 and grid[x][y - 1] >= 0:
            heapq.heappush(q, (grid[x][y - 1], (x, y - 1)))
        if y < len(grid[0]) - 1 and grid[x][y + 1] >= 0:
            heapq.heappush(q, (grid[x][y + 1], (x, y + 1)))
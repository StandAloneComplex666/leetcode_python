class Solution(object):
    def islandPerimeter(self, grid):
        grid_ext = ['0' + ''.join(str(x) for x in row) + '0' for row in grid]
        grid_trans = list(map(list, zip(*grid)))
        grid_ext += [ '0' + ''.join(str(x) for x in row) + '0' for row in grid_trans ]                
        return sum(row.count('01') + row.count('10') for row in grid_ext)
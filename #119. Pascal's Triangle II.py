#119. Pascal's Triangle II
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for row in range(rowIndex):
            cur = [0]+res+[0]
            for col in range(len(cur)-1, 0, -1):
                cur[col] = cur[col] + cur[col-1]
            res = cur[1:]
        return res


class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1, 1]
        list = [[] for i in range(rowIndex+1)]
        list[0] = [1]
        list[1] = [1, 1]
        for i in range(2, rowIndex+1):
            list[i] = [1 for j in range(i + 1)]
            for j in range(1, i):
                list[i][j] = list[i - 1][j - 1] + list[i - 1][j]
        return list[rowIndex]
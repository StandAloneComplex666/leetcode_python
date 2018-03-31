class Solution(object):
    def minDistance(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """
        def taxi(p, q):
            return abs(p[0] - q[0]) + abs(p[1] - q[1])

        S = sum(2 * taxi(tree, nut) for nut in nuts)
        return min(S + taxi(squirrel, nut) - taxi(nut, tree) for nut in nuts)
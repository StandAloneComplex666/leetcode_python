# 492. Construct the Rectangle
class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        w = int(math.sqrt(area))
        while (area%w!=0):
            w-=1
        l = int(area/w)
        return [l,w]
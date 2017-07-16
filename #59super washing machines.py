#517.super wash machines/ 59ms/59.29%
class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        l = len(machines)
        if l<1 or l>10000:
            return -1
        s = sum(machines)
        if s<0 or s>1e5*l:
            return -1
        if s%l != 0:
            return -1
        avg = s/l
        ans = total = 0
        for m in machines:
            total += m - avg
            ans = max(ans, abs(total), m - avg)
        return ans
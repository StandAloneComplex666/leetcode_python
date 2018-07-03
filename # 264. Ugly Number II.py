from heapq import heappush, heappop

class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        q, counted = [1], {1}
        for i in range(n - 1):
            m = heappop(q)
            for mm in [2*m, 3*m, 5*m]:
                if mm not in counted:
                    heappush(q, mm)
                    counted.add(mm)        
        return heappop(q)
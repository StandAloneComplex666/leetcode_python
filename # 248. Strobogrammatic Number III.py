class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        m, n, res, count = len(low), len(high), [], 0
        low, high = int(low), int(high)

        for i in range(m, n+1):
            res += self.findStrobogrammatic(i)

        for i in res:
            if low <= i <= high:
                count += 1
        return count

    def findStrobogrammatic(self, n):
        a = list('018')
        nums = n%2 * list('018') or ['']
        while n > 1:
            n -= 2
            nums = [a + num + b for a, b in '00 11 88 69 96'.split()[n<2:] for num in nums]
        return map(int, nums)
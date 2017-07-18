#204 count prime/256ms/99.62%
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        arr = [True] * n
        arr[0] = arr[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if arr[i]:
                arr[i*i:n:i] = [False] * ((n - 1) // i - i + 1)
        return arr.count(True)  
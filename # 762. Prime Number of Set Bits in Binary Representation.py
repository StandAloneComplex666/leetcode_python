class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        res = 0
        for i in range(L, R+1):
            if self.isPrime(bin(i)[2:].count('1')):
                res += 1
        return res
    
    def isPrime(self, n):
        if n == 2 or n == 3:
            return True
        if n == 1 or n % 2 == 0:
            return False
        for i in range(3, int(n**0.5)+1, 2):
            if n%i == 0:
                return False
        return True
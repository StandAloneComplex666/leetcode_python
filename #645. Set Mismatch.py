#645. Set Mismatch
class Solution(object):
    def findErrorNums(self, A):
        N = len(A)
        count = [0] * (N+1)
        for x in A:
          count[x] += 1
        for x in xrange(1, len(A)+1):
            if count[x] == 2:
                twice = x
            if count[x] == 0:
                never = x
        return twice, never
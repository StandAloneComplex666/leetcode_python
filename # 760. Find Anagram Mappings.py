class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        res = []
        for i in xrange(len(A)):
            j = B.index(A[i])
            res.append(j)
        return res
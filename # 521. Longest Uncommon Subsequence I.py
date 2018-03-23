class Solution(object):
    def findLUSlength(self, A, B):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if A == B:
            return -1
        return max(len(A), len(B))
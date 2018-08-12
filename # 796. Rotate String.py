class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        lenA = len(A)
        lenB = len(B)
        if lenA != len(B):
            return False
        if lenA == 0:
            return True
        if lenA == 1 and A == B:
            return True
        for i in range(1,lenA-1):
            if B[0:i] in A:
                if B[i: len(A)] in A:
                    return True
        return False
class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        res = [len(S) for i in range(len(S))]
        pos = -len(S)
        for i in range(len(S)):
            if S[i] == C:
                pos = i
            res[i] = min(res[i], abs(pos - i))
        for i in range(len(S))[::-1]:
            if S[i] == C:
                pos = i
            res[i] = min(res[i], abs(pos - i))
        return res
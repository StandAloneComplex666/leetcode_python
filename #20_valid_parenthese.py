#39ms \ 89.11ms
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pars = [None]
        parmap = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in parmap:
                if parmap[c] != pars.pop():
                    return False
            else:
                pars.append(c)
        return len(pars) == 1

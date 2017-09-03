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

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        for i in s:
            if i in '([{':
                stk.append(i)
            else:
                if len(stk) == 0:
                    return False
                last = stk.pop()
                if last + i not in ["()", "{}", "[]"]:
                    return False
        return len(stk) == 0

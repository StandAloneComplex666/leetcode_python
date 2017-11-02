class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        history = []
        for c in ops:
            if c<='9' and c>='0':
                history.append(int(c))
            elif c == 'C':
                history.pop()
            elif c == 'D':
                history.append(2*history[-1])
            elif c == '+': 
                history.append(history[-1]+history[-2])
        return sum(history)
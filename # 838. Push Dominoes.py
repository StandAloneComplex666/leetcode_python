class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        dominoes = 'L' + dominoes + 'R'
        res = []
        i = 0
        for j in range(1, len(dominoes)):
            if dominoes[j] == '.': continue
            middle = j - i - 1
            if i: res.append(dominoes[i])
            if dominoes[i] == dominoes[j]: res.append(dominoes[i] * middle)
            elif dominoes[i] == 'L' and dominoes[j] == 'R': res.append('.' * middle)
            else: res.append('R' * (middle / 2) + '.' * (middle % 2) + 'L' * (middle / 2))
            i = j
        return ''.join(res)
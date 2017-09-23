#14. Longest Common Prefix/39ms/82.53%
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        strs.sort()
        res = ''
        for i in xrange(len(strs[0])):
            if i >= len(strs[-1]) or strs[-1][i] != strs[0][i]:
                return res
            res = res + strs[0][i]
        return res
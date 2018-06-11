class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l = len(words)
        indexWord1, indexWord2 = l, l
        ans = l
        for i in xrange(l):
            if words[i] == word1:
                indexWord1 = i
                ans = min(ans, abs(indexWord1 - indexWord2))
            elif words[i] == word2:
                indexWord2 = i
                ans = min(ans, abs(indexWord1 - indexWord2))
            if ans == 1:
                return ans
            #print(ans)
        return ans
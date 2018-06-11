class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.hashmap = {}
        self.length = len(words)
        for i in xrange(len(words)):
            if words[i] not in self.hashmap:
                self.hashmap[words[i]] = [i]
            else:
                self.hashmap[words[i]] += [i]
                

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        list1 = self.hashmap[word1]
        list2 = self.hashmap[word2]
        i, j = 0, 0
        res = self.length
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                res = min(res, list2[j] - list1[i])
                i += 1
            else:
                res = min(res, list1[i] - list2[j])
                j += 1
        return res

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
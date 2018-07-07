class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        hashmap = {}
        res = []
        minIndex = 2001
        for i in xrange(len(list1)):
            hashmap[list1[i]] = i
        for j in xrange(len(list2)):
            if j > minIndex:
                continue
            elif list2[j] in hashmap:
                if hashmap[list2[j]] + j < minIndex:
                    res[:] = []
                    res.append(list2[j])
                    minIndex = hashmap[list2[j]] + j
                elif hashmap[list2[j]] + j == minIndex:
                    res.append(list2[j])
                else:
                    continue
        return res
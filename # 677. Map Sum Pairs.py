# 677. Map Sum Pairs
class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.map[key] = val
        return self.map

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        l = len(prefix)
        sum = 0
        for i in self.map:
            if i[:l] == prefix:
                sum+= self.map[i]
        return sum
                


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
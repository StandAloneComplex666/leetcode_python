# 451. Sort Characters By Frequency

# The best solution I saw using python
class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ''.join(c * i for c, i in collections.Counter(s).most_common())
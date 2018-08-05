class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        charMap = {}
        for i in s:
            if i in charMap:
                charMap[i] += 1
            else:
                charMap[i] = 1
        
        stringSorted = (sorted(charMap.items(), key=lambda t:t[1]))
        res = ""
        for (i,j) in stringSorted:
            temp = i * j
            res += temp
        return res[::-1]
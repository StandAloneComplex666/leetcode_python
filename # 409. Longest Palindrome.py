# my personal version, beat 97.5%!
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        stat = {}
        for char in s:
            if char not in stat:
                stat[char] = 1
            else:
                stat[char] += 1
        res = 0
        flag_odd = 0
        for item in stat:
            #print(stat[item])
            if stat[item]%2 == 0:
                res += stat[item]
            else:
                res += stat[item] - 1
                flag_odd = 1
        return res if flag_odd == 0 else (res+1)




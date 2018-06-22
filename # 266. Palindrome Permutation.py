from collections import Counter
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        odd = 0
        for val in Counter(s).values():
            if val%2: odd += 1
                
        
        return odd < 2
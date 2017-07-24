#125 Valid Palindrome
#62 ms / 92.71%
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alphanumericS = [c for c in s.lower() if c.isalnum()]
        return alphanumericS == alphanumericS[::-1]
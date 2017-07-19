#9 palindrome number
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        def reverse(x):
            answer = 0
            if x < 0:
                return 0
            while x > 0:
                answer = answer * 10 + x % 10
                x /= 10
            if abs(answer) <=2147483647:
                return answer
            else:
                return 0
        if x == reverse(x):
            return True
        else:
            return False
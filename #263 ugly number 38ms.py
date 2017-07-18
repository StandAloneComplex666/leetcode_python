#263 ugly number 38ms
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        
        while num % 2 == 0:
            num /= 2
        
        while num % 3 == 0:
            num /= 3
        
        while num % 5 == 0:
            num /= 5
        
        return num == 1

#version 2 -- my version /69ms
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        if num <= 0:
            return False

        for i in [2, 3, 5]:
            while num%i == 0:
                num = num / i
        return True if num == 1 else False
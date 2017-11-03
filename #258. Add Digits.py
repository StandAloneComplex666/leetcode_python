class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        sum = 0
        flag = 0
        num_2 = num
        while flag == 0:
            sum = 0
            while num_2>0:
                sum+= num_2%10
                num_2=num_2/10
            num_2 = sum
            if num_2 < 10:
                flag = 1
        return sum


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        else:
            return ((num-1)%9 + 1)
        
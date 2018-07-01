class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        numbers={"9":"6","6":"9","8":"8","0":"0","1":"1"}
        
        for i in range((len(num)//2)+1):
            
            if num[i] not in numbers or num[len(num)-i-1] not in numbers:
                return False
            if numbers[num[i]]!=num[len(num)-i-1]:
                return False

        return True
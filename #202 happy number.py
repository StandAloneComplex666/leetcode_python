#202 happy number/36ms/99.10%
def get_next_num(num):
    
    new = 0
    while(num != 0):
        dig = num % 10
        num /= 10
        new += (dig**2)
    
    return new

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        seen_nos = set()
        
        while(True):
            n = get_next_num(n)
            
            if n == 1:
                return True            
            elif n in seen_nos:
                return False
            else:
                seen_nos.add(n)

#my version /59ms /30.04%
class Solution:
    # @param {int} n an integer
    # @return {boolean} true if this is a happy number or false
    def isHappy(self, n):
        # Write your code here
        d = {}
        while True:
            d[n] = 1
            n = sum([int(x) * int(x) for x in list(str(n))])
            if n == 1 or n in d:
                break
        return n == 1
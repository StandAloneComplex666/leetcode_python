#198 house robber
#version 1
class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        size = len(num)
        odd, even = 0, 0
        for i in range(size):
            if i % 2:
                odd = max(odd + num[i], even)
            else:
                even = max(even + num[i], odd)
        return max(odd, even)
#version 2
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        last, now  = 0, 0

        for i in nums:
            now, last = max(i + last, now), now
         
        return now 

#version 3
class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        size = len(num)
        dp = [0] * (size + 1)
        if size:
            dp[1] = num[0]
        for i in range(2, size + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + num[i - 1])
        return dp[size]
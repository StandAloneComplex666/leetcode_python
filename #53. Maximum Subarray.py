# 53. Maximum Subarray/52ms/58.03%
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentSum = maxSum = -1000000000000
        for i in range(len(nums)):
            currentSum = max(nums[i],nums[i]+currentSum)
            maxSum = max(currentSum,maxSum)
        return maxSum
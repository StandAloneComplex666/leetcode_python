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

# another kind of dp method
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
                if nums[i-1] > 0:
                    nums[i] += nums[i-1]
        return max(nums)
# 152. Maximum Product Subarray
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_product = nums[0]
        imin = imax = nums[0]
        for i in xrange(1, len(nums)):
            if nums[i] < 0:
                imin, imax = imax, imin
            imax = max(imax * nums[i], nums[i])
            imin = min(imin * nums[i], nums[i])
            max_product = max(max_product, imax)
        return max_product
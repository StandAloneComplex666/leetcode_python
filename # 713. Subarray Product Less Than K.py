class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 0 or k<=1:
            return 0
        
        start = 0
        end = 0
        res = 0
        prod = 1
        
        while end < len(nums):
            prod *= nums[end]
            end += 1
            while prod >=k:
                prod /= nums[start]
                start += 1
            res += end -start
        return res
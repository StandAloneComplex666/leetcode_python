class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def product(l):
            res = 1
            for i in range(len(l)):
                res *= l[i]
            return res
        
        if len(nums) == 3:
            return product(nums)
        if len(nums) == 4:
            max1 = nums.pop(nums.index(max(nums)))
            max2 = nums.pop(nums.index(max(nums)))
            min1 = nums.pop(nums.index(min(nums)))
            min2 = nums.pop(nums.index(min(nums)))
            return max(max1*max2*min2, min1*min2*max1)
        max1 = nums.pop(nums.index(max(nums)))
        max2 = nums.pop(nums.index(max(nums)))
        max3 = nums.pop(nums.index(max(nums)))
        min1 = nums.pop(nums.index(min(nums)))
        min2 = nums.pop(nums.index(min(nums)))
        
        return max(max1*max2*max3, min1*min2*max1)
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if target == nums[i]:
                return nums.index(target)
            elif target < nums[i]:
                return i
        return i+1
                

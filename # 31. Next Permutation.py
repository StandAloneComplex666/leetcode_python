class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1: return
        index = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i+1] > nums[i]:
                index = i
                break
        if index == -1: 
            nums[:] = nums[::-1]
            return
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                break
        nums[index+1:] = nums[index+1:][::-1]
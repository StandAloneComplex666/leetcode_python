class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp_sum = 0
        max_sum = 0
        if not nums:
             return max_sum
        nums_temp = nums + [0] 
        for i in range(len(nums_temp)):
            if nums_temp[i] == 1:
                temp_sum += 1
            else:
                max_sum = max(max_sum, temp_sum)
                temp_sum = 0
        return max_sum
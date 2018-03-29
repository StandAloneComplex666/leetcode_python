class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        accum_dict = {0:-1}
        max_length = 0
        count = 0
        for i in xrange(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                count += -1
                
            if count in accum_dict:
                max_length = max(max_length, i - accum_dict[count])
            else:
                accum_dict[count] = i
        return max_length
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        length = len(nums)
        sum_step = 0
        for i in xrange(length):
            if i<length - i -1:
                sum_step += nums[length - i -1] - nums[i]
        return sum_step
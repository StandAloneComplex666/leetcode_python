# 153. Find Minimum in Rotated Sorted Array
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l , h = 0 , len(nums)-1
        while l < h:
            m= (l + h )/2
            if nums[m] < nums[h]:
                h = m
            else:
                l =m + 1
        return nums[l]
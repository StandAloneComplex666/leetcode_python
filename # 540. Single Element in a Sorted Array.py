# 540. Single Element in a Sorted Array
class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        l = len(nums)
        if l == 1:
            return nums[0]
        low = 0
        high = l-1
        while(low < high):
            mid = int((low + high)/2)
            #print("mid =",mid)
            #this if part could be replaced by target = mid^1
            if mid%2 == 0:
                target = mid+1
            else:
                target = mid-1
            #print("target = ",target)
            if nums[mid]==nums[target]:
                low =mid+1
            else:
                high = mid
            #print(low," ",high)
        return nums[low]


#268. Missing Number 
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n*(n+1)/2 - sum(nums)

#my version
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = 0
        nums = sorted(nums)
        if nums[0] != 0 :
            return 0
        for i in range(1,len(nums)):
            if nums[i] != pre + 1:
                return pre + 1
            pre = pre + 1
        return len(nums)
            
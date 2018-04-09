class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {0:-1}
        r = 0
        for i in range(len(nums)):
            r = (r+nums[i])%k if k else r+nums[i]
            if r not in seen:
                seen[r] = i
            if i -seen[r] > 1:
                return True
        return False
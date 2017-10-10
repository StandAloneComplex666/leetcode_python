#643. Maximum Average Subarray I
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max = tmp = sum(nums[0:k])
        for i in range(k,len(nums)):
            tmp = tmp + nums[i] - nums[i-k]
            if tmp > max:
                max = tmp
        return float(max)/float(k)


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if not nums:
            return -1.0
        max_nums = -10000.0
        sum_nums = 0.0
        for i in xrange(0,len(nums)):
            sum_nums+= nums[i]
            if i>=k:
                sum_nums-=nums[i-k]
            if i>=k-1:
                max_nums = max(max_nums, 1.0*sum_nums/k)
        return max_nums
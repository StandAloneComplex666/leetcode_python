# 169. Majority Element
# version 1
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums)/2]

# version 2
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate , count = None , 0
        for i in nums:
            if count == 0:
                candidate ,count = i , 1
            elif i == candidate:
                count  = count + 1
            else:
                count  = count - 1
        return candidate
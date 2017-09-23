#217. Contains Duplicate
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        map = {}
        for i in nums:
            if i in map:
                return True
            map[i] = True
        return False
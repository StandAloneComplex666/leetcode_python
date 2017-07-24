#
# fastest version : use data structure set
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        return list(set(nums1) & set(nums2))

# my version : like a prototype of intersection
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        if nums1 == [] or nums2 == []:
            return res
        for i in nums1:
            if i in nums2 and i not in res:
                res.append(i)
        return res
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        d = {}
        
        for i in nums2:
            while stack and stack[-1]<i:
                d[stack.pop()] = i
            stack.append(i)
        
        while stack:
            d[stack.pop()] = -1
            
        res = []
        for i in nums1:
            res.append(d[i])
        return res
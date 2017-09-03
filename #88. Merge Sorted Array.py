#88. Merge Sorted Array
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        tmp = [0 for i in range(m + n)]
        i = 0; j = 0; k = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                tmp[k] = nums1[i]; i += 1
            else:
                tmp[k] = nums2[j]; j += 1
            k += 1
        if i == m:
            while k < m + n:
                tmp[k] = nums2[j]; k += 1; j += 1
        else:
            while k < m + n:
                tmp[k] = nums1[i]; i += 1; k += 1
        for i in range(0, m + n):
            nums1[i] = tmp[i]
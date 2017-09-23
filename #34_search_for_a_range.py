# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 19:46:03 2017

@author: hp
"""

class Solution():
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        c = 0
        for i in range(len(nums)):
            if (c == 1) and (nums[i] == target):
                res.append(i)
                return res
            elif (c == 0) and (nums[i] == target):
                res.append(i)
                c = c + 1
        res=[-1,1]        
        return res
        
if __name__=='__main__':
    s=Solution()
    nums=[5,7,7,8,8,10]
    target=8
    result=s.searchRange(nums,target)
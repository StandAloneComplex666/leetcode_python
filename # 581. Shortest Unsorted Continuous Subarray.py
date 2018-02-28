# time complexity:O(nlgn)
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        i, n = 0, len(nums)-1
        sorted_nums= sorted(nums)
        while nums[i] == sorted_nums[i]:
            i += 1
            if i >= len(nums)-1:
                break
        while nums[n] == sorted_nums[n]:
            n -= 1
            if n <= i:
                break
        return n-i+1 

# time complexity:O(n)
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       #if len(nums) == 1:
       #    return 0
        start, end, n = -1, -2, len(nums)
        mn, mx = nums[n-1], nums[0]
        for  i in range(n):
            mx = max(mx, nums[i])
            mn = min(mn, nums[n-i-1])
            if mx > nums[i]: 
                end = i
            if mn < nums[n-i-1]:
                start = n-i-1
        return end-start+1
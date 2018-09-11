# first version which does not use O(1) space:
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numStart = 0
        numEnd = 0
        l = len(nums)
        listEnd = l
        for i in range(l):
            if nums[i] == nums[i-1]:
                numEnd += 1
            else:
                distance = numEnd - numStart + 1
                if distance > 2:
                    nums = nums[0:numStart+2] + nums[numEnd+1:] + nums[numStart+2:numEnd+1]
                    listEnd -= distance-2
                    #print(nums, listEnd)
                numStart = i
                numEnd = i
            if numStart > listEnd - 2:
                #print(nums)
                break
        return listEnd

# Second Version:
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        if len(nums) < 3:
            return len(nums)
        i = 1
        start = 1
        count = 0
        while i < len(nums):
            if nums[i] == nums[i-1]:
                count += 1
                if count >= 2:
                    i += 1
                    continue
            else:
                count = 0
            nums[start] = nums[i]
            start += 1
            i += 1
        return start
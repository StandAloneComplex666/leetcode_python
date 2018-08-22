class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i] < stack[-1] and nums[i] > 0:
                stack.append[nums[i]]
        print(stack)
        if stack[-1] != 1:
            return 1
        elif len(stack) == 1:
            return 2
        else:
            pre1 = stack.pop()
            while stack:
                pre2 = stack.pop()
                if pre2 != pre1+1:
                    return pre1+1
                pre1 = pre2
            return pre1+1
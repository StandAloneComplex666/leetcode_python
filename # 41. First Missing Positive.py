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



        n = len(nums)
        i = 0
        if n == 0: 
            return 1
        while i < n:
            while nums[i] != i + 1 and nums[i] <= n and nums[i] > 0 and nums[i] != nums[nums[i] - 1]: 
                t = nums[i]
                nums[i] = nums[nums[i] - 1] 
                nums[t - 1] = t
            i = i + 1
        for i in range(n):
            if nums[i] != i + 1: return i + 1
        return n + 1

        l = len(nums)
        if l == 0:
            return 1
        for i in range(l):
            if nums[i] > 0 and nums[i] <= l and nums[i] != nums[nums[i] - 1] and nums[i] != i+1:
                print(nums[i], nums[nums[i]-1])
                temp = nums[i]
                nums[i] = nums[nums[i]-1]
                nums[nums[i]-1] = temp

        for i in range(l):
            if nums[i] != i+1:
                return i+1
        return l+1
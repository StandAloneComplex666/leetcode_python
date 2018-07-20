class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = [float("-inf")] + nums + [float("inf")]
        count = 0
        
        for i in range(1, len(nums)-1):
            
            if nums[i] > nums[i+1]:
                index = i
                count += 1
                if count == 2:
                    return False
                
        if count == 0: return True
        
        if count == 1 and nums[index-1]<= nums[index+1]: return True
        
        if count == 1 and nums[index] <= nums[index+2]: return True
                            
        return False
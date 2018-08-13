class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        while low <= high:
            mid = int((low + high)/2)
            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[low]:
                if target < nums[mid] and target >= nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] < nums[low]:
                if target > nums[mid] and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
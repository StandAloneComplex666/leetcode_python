class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp_num = [];
        latest = -1
        sum = 0;
        for val in nums[0:len(nums)]:
            sum = sum + val;
            temp_num.append(sum);
        
        sum = 0;
        idx = len(nums)-1;
        for val in nums[::-1]:
            sum = sum + val;
            if sum == temp_num[idx]:
                latest = idx;
            idx = idx - 1;
            
        return latest;
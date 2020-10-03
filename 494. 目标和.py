class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        def dfs(nums, curr_index, curr_sum, target):
            if curr_index == len(nums):
                return int(curr_sum==target)
            else:
                return dfs(nums, curr_index+1, curr_sum - nums[curr_index], target) +   dfs(nums, curr_index+1, curr_sum + nums[curr_index], target) 
        return dfs(nums, 0, 0, S)
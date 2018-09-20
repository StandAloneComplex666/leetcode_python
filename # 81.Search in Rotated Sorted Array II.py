# 内置函数牛逼！ beat98%...
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if target in nums:
            return True
        else:
            return False

# 正常logn解法：（beat 99.8%）
# 思路 ： 判断哪个半边是正常排序的
# 若 最左边元素小于中间元素 则左半边是已排序的 对这半边用普通二分查找 对另外半边递归或者执行之前同样步骤
# 反之 则操作左右对调
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            while l < mid and nums[l] == nums[mid]: # tricky part
                l += 1
            # the first half is ordered
            if nums[l] <= nums[mid]:
                # target is in the first half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # the second half is ordered
            else:
                # target is in the second half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
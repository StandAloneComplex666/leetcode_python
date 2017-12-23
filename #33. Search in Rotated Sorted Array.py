#33. Search in Rotated Sorted Array
'''Explanation
My solutions use binary search guided by the following thoughts:

Remember the array is sorted, except it might drop at one point.

If nums[0] <= nums[i], then nums[0..i] is sorted (in case of "==" it's just one element, and in case of "<" there must be a drop elsewhere). So we should keep searching in nums[0..i] if the target lies in this sorted range, i.e., if nums[0] <= target <= nums[i].

If nums[i] < nums[0], then nums[0..i] contains a drop, and thus nums[i+1..end] is sorted and lies strictly between nums[i] and nums[0]. So we should keep searching in nums[0..i] if the target doesn't lie strictly between them, i.e., if target <= nums[i] < nums[0] or nums[i] < nums[0] <= target

Those three cases look cyclic:

    nums[0] <= target <= nums[i]
               target <= nums[i] < nums[0]
                         nums[i] < nums[0] <= target
So I have the three checks (nums[0] <= target), (target <= nums[i]) and (nums[i] < nums[0]), and I want to know whether exactly two of them are true. They can't all be true or all be false (check it), so I just need to distinguish between "two true" and "one true". Parity is enough for that, so instead of adding them I xor them, which is a bit shorter and particularly helpful in Java and Ruby, because those don't let me add booleans but do let me xor them.

(Actually while developing this I thought of permutations of nums[0], target and nums[i] and the permutation parity and saw those three checks as representing inversions, but I had trouble putting that into words and now find the above explanation much better. But it helped me get there, so I wanted to mention it here.)'''
class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, nums, target):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) / 2
            if (nums[0] > target) ^ (nums[0] > nums[mid]) ^ (target > nums[mid]):
                lo = mid + 1
            else:
                hi = mid
        return lo if target in nums[lo:lo+1] else -1
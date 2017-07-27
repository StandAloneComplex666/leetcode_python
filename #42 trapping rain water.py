#42.trapping rain water 45ms/83.33%
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_left = max_right = ans = 0
        L, R = 0, len(height) - 1
        while L < R:
            if height[L] <= height[R]:
                max_left = max(max_left, height[L])
                ans += max_left - height[L]
                L += 1
            else:
                max_right = max(max_right, height[R])
                ans += max_right - height[R]
                R -= 1
        return ans
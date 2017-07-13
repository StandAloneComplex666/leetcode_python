#11. Container With Most Water /66ms/85.95%
class Solution(object):
    '''
    题意:任取两个a[i]、a[j] 使得min(a[i], a[j]) * abs(i - j)最大化
    用两个指针从两侧向中间扫描，每次移动数值较小的指针，用反证法可以证明
    总是可以得到最优答案
    '''
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        ans = 0
        while left != right:
            if height[left] < height[right]:
                area = height[left] * (right - left)
                left += 1
            else:
                area = height[right] * (right - left)
                right -= 1
            ans = max(ans, area) 
        return ans
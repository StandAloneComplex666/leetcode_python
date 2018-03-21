class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = [-1]
        largest = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                current_height = heights[stack.pop()]
                width = i - stack[-1] - 1
                area = width * current_height
                largest = max(area, largest)
            stack.append(i)
        heights.pop()
        return largest
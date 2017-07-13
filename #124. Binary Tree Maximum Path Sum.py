#124. Binary Tree Maximum Path Sum / 169ms/ 47.62%
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.path_sum = []

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self._max_path_sum(root)
        return max(self.path_sum)

    def _max_path_sum(self, root):
        if not root:
            return False
        left = self._max_path_sum(root.left)
        right = self._max_path_sum(root.right)

        if not left or left + root.val < root.val:
            left = 0
        if not right or right + root.val < root.val:
            right = 0

        path_sum = root.val + left +right
        self.path_sum.append(path_sum)
        return left + root.val if left > right else right + root.val
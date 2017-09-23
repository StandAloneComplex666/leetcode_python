#119ms/ 80.63%
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # 结点都为空时
        if t1 is None and t2 is None:
            return
        # 只有一个结点为空时
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        # 结点重叠时
        t1.val += t2.val
        # 进行迭代
        t1.right = self.mergeTrees(t1.right, t2.right)
        t1.left = self.mergeTrees(t1.left, t2.left)
        return t1
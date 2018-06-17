# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        def helper(node,target,minval,maxval):
            if node is None:
                if (maxval-target > target-minval):
                    return minval
                else:
                    return maxval
            if target < node.val:
                return helper(node.left,target,minval,node.val)
            else:
                return helper(node.right,target,node.val,maxval)

        return helper(root,target,float('-inf'),float('inf'))
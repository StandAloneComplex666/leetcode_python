#55ms / 26.12%
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sum(self, root, preSum):
        if root==None: return 0
        preSum = preSum*10 + root.val
        if root.left==None and root.right==None: return preSum
        return self.sum(root.left, preSum)+self.sum(root.right, preSum)
        
    def sumNumbers(self, root):
        return self.sum(root, 0)
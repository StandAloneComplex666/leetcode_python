# 98. Validate Binary Search Tree /69ms / 79.57%
class Solution:
    # @param root, a tree node
    # @return a boolean
    def ValidBST(self, root, min, max):
        if root == None:
            return True
        if root.val <= min or root.val >= max:
            return False
        return self.ValidBST(root.left, min, root.val) and self.ValidBST(root.right, root.val, max)
    
    def isValidBST(self, root):
        return self.ValidBST(root, -2147483648, 2147483647)

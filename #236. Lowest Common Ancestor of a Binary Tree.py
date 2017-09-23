#236. Lowest Common Ancestor of a Binary Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or p==root or q==root:
            return root
        if self.isnode(p,q):
            return p
        if self.isnode(p,q):
            return q
        if self.isnode(root.left,p) and self.isnode(root.left,q):
            return self.lowestCommonAncestor(root.left,p,q)
        if self.isnode(root.right,p) and self.isnode(root.right,q):
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root
    def isnode(self,mother,child):
        if mother:
            if mother==child:
                return True
            else:
                return self.isnode(mother.left,child) or self.isnode(mother.right,child)
        return False  

#32ms / 92.56%
# Definition for a  binary tree node  
# class TreeNode:  
#     def __init__(self, x):  
#         self.val = x  
#         self.left = None  
#         self.right = None  
  
class Solution:  
    # @param p, a tree node  
    # @param q, a tree node  
    # @return a boolean  
    def isSameTree(self, p, q):  
        if p is None and q is None:  
            return True  
        elif p is None or q is None:  
            return False  
        else:  
            if p.val == q.val:  
                if self.isSameTree(q.left,p.left):  
                    return self.isSameTree(p.right,q.right)  
            return False  
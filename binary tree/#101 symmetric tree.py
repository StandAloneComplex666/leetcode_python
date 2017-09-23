# 101 symmetric tree / version 1 recursion 23%
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def help(self, p, q):
        if p == None and q == None: return True
        if p and q and p.val == q.val:
            return self.help(p.right, q.left) and self.help(p.left, q.right)
        return False
    
    def isSymmetric(self, root):
        if root:
            return self.help(root.left, root.right)
        return True

# version 2 DFS 79%
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stackl, stackr = [root.left], [root.right]
        while len(stackl) > 0 and len(stackr) > 0:
            left = stackl.pop()
            right = stackr.pop()
            if not left and not right:
                continue
            elif not left or not right:
                return False
            if left.val != right.val:
                return False
            stackl.append(left.left)
            stackl.append(left.right)
            stackr.append(right.right)
            stackr.append(right.left)
        return len(stackl) == 0 and len(stackr) == 0

# version 3 BFS / 74%
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        queuel, queuer = [root.left], [root.right]
        while len(queuel) > 0 and len(queuer) > 0:
            left = queuel.pop()
            right = queuer.pop()
            if not left and not right:
                continue
            elif not left or not right:
                return False
            if left.val != right.val:
                return False
            queuel.insert(0, left.left)
            queuel.insert(0, left.right)
            queuer.insert(0, right.right)
            queuer.insert(0, right.left)
        return len(queuel) == 0 and len(queuer) == 0
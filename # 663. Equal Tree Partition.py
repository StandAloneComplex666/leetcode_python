# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.dmap = {}
        def solve(n, c):
            if not n: return 0
            self.dmap[c] = n.val + solve(n.left, c * 2) + solve(n.right, c * 2 + 1)
            return self.dmap[c]
        solve(root, 1)
        total = self.dmap[1]
        del self.dmap[1]
        return any(v * 2 == total for k, v in self.dmap.iteritems())
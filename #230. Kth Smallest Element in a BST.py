#230. Kth Smallest Element in a BST
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        #inorder tranverse
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                node = stack.pop()
                k -= 1
                if k == 0:
                    return node.val
                root = node.right
        return None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count = []
        self.helper(root, count)
        return count[k-1]
        
    def helper(self, node, count):
        if not node:
            return
        
        self.helper(node.left, count)
        count.append(node.val)
        self.helper(node.right, count)
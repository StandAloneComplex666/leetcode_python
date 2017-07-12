#144. Binary Tree Preorder Traversal  / 32ms /94.93%
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def iterative_preorder(self, root, list):
        stack = []
        while root or stack:
            if root:
                list.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        return list
    
    def recursive_preorder(self, root, list):
        if root:
            list.append(root.val)
            self.preorder(root.left,list)
            self.preorder(root.right,list)

    def preorderTraversal(self,root):
        list = []
        self.iterative_preorder(root,list)
        return list
        
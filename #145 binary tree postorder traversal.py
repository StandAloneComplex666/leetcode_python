#145. Binary Tree Postorder Traversal/ 32ms/92.42%
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def recursive_postorder(self, root, list):
        if root:
            self.postorder( root.left, list )
            self.postorder( root.right, list )
            list.append(root.val)
    
    def iterative_postorder(self, root, list):
        stack = []
        pre = None
        if root:
            stack.append(root)
            while stack:
                curr = stack[len(stack) - 1]
                if (curr.left == None and curr.right == None) or (pre and (pre == curr.left or pre == curr.right)):
                    list.append(curr.val)
                    stack.pop()
                    pre = curr
                else:
                    if curr.right: stack.append(curr.right)
                    if curr.left: stack.append(curr.left)
        return list

    def postorderTraversal(self, root):
        list = []
        self.iterative_postorder(root,list)
        return list
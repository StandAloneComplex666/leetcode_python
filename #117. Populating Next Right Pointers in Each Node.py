#117. Populating Next Right Pointers in Each Node II/ 92ms / 82.51%
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root:
            p = root; q = None; nextNode = None
            while p:
                if p.left:
                    if q: q.next = p.left
                    q = p.left
                    if nextNode == None: nextNode = q
                if p.right:
                    if q: q.next = p.right
                    q = p.right
                    if nextNode == None: nextNode = q
                p = p.next
            self.connect(nextNode)
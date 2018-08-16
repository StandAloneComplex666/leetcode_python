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


# a new version which is implemented by iteration, not recursion
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
        curr = root
        while curr:
            firstNext = None
            prev = None
            while curr:
                if not firstNext:
                    firstNext = curr.left if curr.left else curr.right
                if curr.left:
                    if prev:prev.next = curr.left
                    prev = curr.left
                if curr.right:
                    if prev:prev.next = curr.right
                    prev = curr.right
                curr = curr.next
            curr = firstNext

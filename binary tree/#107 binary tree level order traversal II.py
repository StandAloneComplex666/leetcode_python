#107 binary tree level order traversal II/42ms/95.73%
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root == None:
            return res
        q = []
        q.append(root)
        while(len(q)!=0):
            tmp = []
            len_q = len(q)
            for i in range(len_q):
                node = q[0]
                del q[0]
                tmp.append(node.val)
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            res.append(tmp)
        return res[::-1]
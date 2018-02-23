# 337. House Robber III
# first version : bruteforce DFS ,TLE
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_val = 0
        if root == None:
            return max_val
        if root.left != None:
            max_val += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right != None:
            max_val += self.rob(root.right.left) + self.rob(root.right.right)
        return max(max_val + root.val,self.rob(root.left) + self.rob(root.right))

# second edition: use DP to overcome the overlapping problem -- 78ms , 37.71%
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.subrob(root, hashmap={})
    def subrob(self, root, hashmap):
        max_val = 0
        if root == None:
            return max_val
        if root in hashmap:
            return hashmap[root]
        if root.left != None:
            max_val += self.subrob(root.left.left, hashmap) + self.subrob(root.left.right, hashmap)
        if root.right != None:
            max_val += self.subrob(root.right.left, hashmap) + self.subrob(root.right.right, hashmap)
        max_val = max(max_val + root.val, self.subrob(root.left, hashmap) + self.subrob(root.right, hashmap))
        hashmap[root] = max_val
        return max_val

 #third edition: by keeping track of the information of both scenarios, it changes to a greedy problem -- 70ms, 62.21%
#actully, I found the fastest version and it test time is 100%,then it shows and it has very similar idea with this edition
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = self.subrob(root)
        return max(res[0], res[1])
    def subrob(self, root):
        max_val = 0
        if root == None:
            res =[0,0]
            return res

        left = self.subrob(root.left)
        right = self.subrob(root.right)
        res = []
        
        res.append(max(left[0], left[1]) + max(right[0], right[1]))
        res.append(root.val + left[0] + right[0])
        return res

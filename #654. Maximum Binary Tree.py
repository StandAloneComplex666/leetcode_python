#654. Maximum Binary Tree

# my version , very slow 205ms  
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        max_nums = max(nums)
        index = nums.index(max_nums)
        root = TreeNode(None)
        root.val = max_nums
        root.left = self.constructMaximumBinaryTree(nums[:index])
        root.right = self.constructMaximumBinaryTree(nums[index+1:])
        return root

# other's version use stack to do it O(n)(likely?),but at least a great idea!
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        if not nums: return
        stack = []
        for i in nums:
            curr = TreeNode(i)
            while stack and stack[-1].val < i:
                curr.left = stack.pop()
            if stack:
                stack[-1].right = curr
            stack.append(curr)
        return stack[0]
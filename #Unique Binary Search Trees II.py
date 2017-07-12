#have some problems with test results
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:  
    # @return a list of tree node  
    def getTree(self,start,end):  
        if start>end:  
            return [None]  
        solution=[]  
        for rootval in range(start,end+1):  
            left=self.getTree(start,rootval-1)  
            right=self.getTree(rootval+1,end)  
            for i in left:  
                for j in right:  
                    root=TreeNode(rootval)  
                    root.left=i  
                    root.right=j  
                    solution.append(root)  
        return solution              
    def generateTrees(self, n):  
        return self.getTree(1,n)  
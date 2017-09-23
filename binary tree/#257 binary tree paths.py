#46ms /71.03%
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths
    def binaryTreePaths(self, root):
        # Write your code here
        result = []
        if root is None:
            return result
        self.dfs(root, result, [])
        return result

    def dfs(self, node, result, tmp):
        tmp.append(str(node.val))
        if node.left is None and node.right is None:
            result.append('->'.join(tmp))
            tmp.pop()
            return

        if node.left:
            self.dfs(node.left, result, tmp);
        
        if node.right:
            self.dfs(node.right, result, tmp)

        tmp.pop()
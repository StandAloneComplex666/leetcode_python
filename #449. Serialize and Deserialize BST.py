#449. Serialize and Deserialize BST
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        arr = []
        def _serialize(node):
            if node == None:
                arr.append('#')
                return 
            arr.append(str(node.val))
            _serialize(node.left)
            _serialize(node.right)
        _serialize(root)
        return ','.join(arr)
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def _deserialize():
            c = next(vals)
            if c == '#':
                return None
            node = TreeNode(c)
            node.left = _deserialize()
            node.right = _deserialize()
            return node
        vals = iter(data.split(','))
        return _deserialize()
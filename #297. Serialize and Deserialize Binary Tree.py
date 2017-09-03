#297. Serialize and Deserialize Binary Tree
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        q, ans = [], []
        q.append(root)
        while q:
            cur = q.pop(0)
            if cur:
                ans.append(cur.val)
                q.append(cur.left)
                q.append(cur.right)
            else:
                ans.append(None)
        return ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data or data[0] is None: return None
        q = []
        root = cur = TreeNode(data[0])
        for i in xrange(1, len(data)):
            if data[i] is None:
                if not i & 1 and q:
                    cur = q.pop(0)
                continue

            node = TreeNode(data[i])
            q.append(node)

            if i & 1:  # left son
                cur.left = node
            else:
                cur.right = node
                cur = q.pop(0)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))